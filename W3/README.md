-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `zoomcamp.external_yellow_tripdata`
OPTIONS (
  format = 'parquet',
  uris = ['gs://popof-zoomcamp-kestra/yellow_tripdata_2024-*.parquet']
);

-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE `zoomcamp.external_yellow_tripdata_non_partitioned` AS
SELECT * FROM `zoomcamp.external_yellow_tripdata`;

-- Q1
SELECT COUNT(*) from `zoomcamp.external_yellow_tripdata`;
SELECT COUNT(*) from `zoomcamp.external_yellow_tripdata_non_partitioned`;

--Q2
SELECT DISTINCT(PULocationID) FROM `zoomcamp.external_yellow_tripdata`;
SELECT DISTINCT(PULocationID) FROM `zoomcamp.external_yellow_tripdata_non_partitioned`;

--Q3
SELECT PULocationID FROM `zoomcamp.external_yellow_tripdata_non_partitioned`;
SELECT PULocationID, DOLocationID FROM `zoomcamp.external_yellow_tripdata_non_partitioned`;

--Q4
SELECT COUNT(*)
FROM `zoomcamp.external_yellow_tripdata_non_partitioned`
WHERE fare_amount=0;

--Q5
CREATE OR REPLACE TABLE `zoomcamp.external_yellow_tripdata_partitioned`
PARTITION BY
  DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `zoomcamp.external_yellow_tripdata`;

--Q6
SELECT DISTINCT(VendorID) FROM `zoomcamp.external_yellow_tripdata_non_partitioned`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';

SELECT DISTINCT(VendorID) FROM `zoomcamp.external_yellow_tripdata_partitioned`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';
