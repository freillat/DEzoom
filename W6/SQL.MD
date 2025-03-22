CREATE TABLE processed_events_aggregated (
            PULocationID INTEGER,
            DOLocationID INTEGER,
            num_trips BIGINT,
            streak_duration BIGINT
);

SELECT PULocationID, DOLocationID, streak_duration
FROM processed_events_aggregated
GROUP BY PULocationID, DOLocationID, streak_duration
order BY streak_duration DESC;