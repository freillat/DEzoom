Windows command line to ingest data

$env:URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz"

python ingest_data.py `
   --user=postgres `
   --password=postgres `
   --host=localhost `
   --port=5433 `
   --db=ny_taxi `
   --table_name=green_taxi_trips `
   --url=$env:URL

$env:URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

python ingest_data.py `
   --user=postgres `
   --password=postgres `
   --host=localhost `
   --port=5433 `
   --db=ny_taxi `
   --table_name=taxi_zone `
   --url=$env:URL


Question 4:
SELECT lpep_pickup_datetime, MAX(trip_distance) AS TRIP
FROM green_taxi_trips
GROUP BY lpep_pickup_datetime
ORDER BY TRIP DESC;

Question 5:
SELECT "Zone", COUNT(*)
FROM green_taxi_trips gtt
JOIN taxi_zone tz ON gtt."PULocationID" = tz."LocationID"
WHERE DATE(lpep_pickup_datetime) = '2019-10-18'
GROUP BY "Zone"
HAVING SUM(total_amount) > 13000
ORDER BY "count" DESC;

Question 6:
SELECT MAX(gtt."tip_amount"), tz."Zone"
FROM green_taxi_trips gtt
JOIN taxi_zone tz ON gtt."DOLocationID" = tz."LocationID"
WHERE DATE(lpep_pickup_datetime) >= '2019-10-01'
	AND DATE(lpep_pickup_datetime) <= '2019-10-31' 
	AND gtt."PULocationID" = (
		SELECT "LocationID"
		FROM taxi_zone
		WHERE "Zone" = 'East Harlem North'
	) 
GROUP BY "Zone"
ORDER BY "max" DESC;