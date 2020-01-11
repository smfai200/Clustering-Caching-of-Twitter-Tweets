from django.shortcuts import render
import os
import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from Caching.models import Data,Data_Serializer


def GetClustersLength():
    datadir =  os.path.realpath('../results')
    files = os.listdir(datadir)
    clusters_length = len(files)
    return clusters_length

def PreCache():
    print("Pre Caching Active")
    clusters = list(Data.objects.order_by().values('cluster').distinct().values_list('cluster')[:5])
    kmeans_clusters = list(Data.objects.order_by().values('mb_cluster').distinct().values_list('mb_cluster')[:5])
    dbscan_clusters = list(Data.objects.order_by().values('db_cluster').distinct().values_list('db_cluster')[:5])

    clusters_ = []
    kmeans_clusters_ = []
    dbscan_clusters_ = []

    for i in range(0,5):
        clusters_.append(clusters[i][0])
        kmeans_clusters_.append(kmeans_clusters[i][0])
        dbscan_clusters_.append(dbscan_clusters[i][0])


    print("Clusters: ", clusters_)
    print("DBSCANClusters: ", dbscan_clusters_)
    print("KMEANSClusters: ", kmeans_clusters_)

    for j in range(0,5):
        kmeans_data = Data.objects.filter(mb_cluster=kmeans_clusters_[j]).order_by('-popularity')[:15]
        dbscan_data = Data.objects.filter(db_cluster=dbscan_clusters_[j]).order_by('-popularity')[:15]
        cluster_data = Data.objects.filter(cluster=clusters_[j]).order_by('-popularity')[:15]
        cache.set("cluster"+str(clusters_[j]), cluster_data, 240)
        cache.set("kmeans"+str(kmeans_clusters_[j]), kmeans_data, 240)
        cache.set("dbscan"+str(dbscan_clusters_[j]), dbscan_data, 240)

    print("Popular Content Cached Initiatiated for Kmeans, DBSCAN, HDBSCAN")
    return

class HomePage(View):
    template_name = 'HomeCluster.html'

    def get(self, request, *args, **kwargs):
        clusters = GetClustersLength
        values = list(range(0,clusters))
        return render(request, self.template_name, {"clusters":values})


class dbscan_CachedAccess(APIView):
    def get(self, request, *args, **kwargs):
        Clusterid = request.GET["Cluster"]
        cached_tweets = cache.get("dbscan"+str(Clusterid))
        data = Data_Serializer(cached_tweets, many=True)
        return Response(data.data)

class dbscan_NonCachedAccess(APIView):
    def get(self, request, *args, **kwargs):
        Clusterid = request.GET["Cluster"]
        uncached_tweets = Data.objects.filter(cluster=float(Clusterid)).order_by('-popularity')[:15]
        data = Data_Serializer(uncached_tweets,many=True)
        return Response(data.data)

class kmeans_CachedAccess(APIView):
    def get(self, request, *args, **kwargs):
        Clusterid = request.GET["Cluster"]
        cached_tweets = cache.get("kmeans"+str(Clusterid))
        data = Data_Serializer(cached_tweets, many=True)
        return Response(data.data)

class kmeans_NonCachedAccess(APIView):
    def get(self, request, *args, **kwargs):
        Clusterid = request.GET["Cluster"]
        uncached_tweets = Data.objects.filter(cluster=float(Clusterid)).order_by('-popularity')[:15]
        data = Data_Serializer(uncached_tweets,many=True)
        return Response(data.data)

class CachedAccess(APIView):
    def get(self, request, *args, **kwargs):
        Clusterid = request.GET["Cluster"]
        cached_tweets = cache.get("cluster"+str(Clusterid))
        print("cluster"+str(Clusterid))
        data = Data_Serializer(cached_tweets, many=True)
        return Response(data.data)

class NonCachedAccess(APIView):
    def get(self, request, *args, **kwargs):
        Clusterid = request.GET["Cluster"]
        uncached_tweets = Data.objects.filter(cluster=float(Clusterid)).order_by('-popularity')[:15]
        data = Data_Serializer(uncached_tweets,many=True)
        return Response(data.data)