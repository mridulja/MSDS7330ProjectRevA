# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os 
import sys

os.environ['SPARK_HOME']="C:/spark/spark-1.5.1-bin-hadoop2.6"

sys.path.append("C:/spark/spark-1.5.1-bin-hadoop2.6/bin") 
sys.path.append("C:/spark/spark-1.5.1-bin-hadoop2.6/python") 
sys.path.append("C:/spark/spark-1.5.1-bin-hadoop2.6/python/pyspark/") 
sys.path.append("C:/spark/spark-1.5.1-bin-hadoop2.6/python/lib") 
sys.path.append("C:/spark/spark-1.5.1-bin-hadoop2.6/python/lib/pyspark.zip")
sys.path.append("C:/spark/spark-1.5.1-bin-hadoop2.6/python/lib/pyspark.zip")
sys.path.append("C:/spark/spark-1.5.1-bin-hadoop2.6/python/lib/py4j-0.8.2.1-src.zip")

from pyspark import SparkContext 
from pyspark import SparkConf

print os.getcwd()
os.chdir("C:\spark\spark-1.5.1-bin-hadoop2.6")
print os.getcwd()

logFile = "README.md"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))