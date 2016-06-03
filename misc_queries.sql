# Misc SQL Queries:

# Find most popular hotel_cluster given srch_destination_id
select srch_destination_id, hotel_cluster, count(hotel_cluster) as hotel_cluster_cnt
from train
group by srch_destination_id, hotel_cluster, is_booking
order by srch_destination_id ASC, hotel_cluster_cnt DESC

# Same as above, but with srch_destination_type_id
select srch_destination_type_id, hotel_cluster, count(hotel_cluster) as hotel_cluster_cnt
from train
group by srch_destination_type_id, hotel_cluster
order by srch_destination_type_id ASC, hotel_cluster_cnt DESC

# By user_location_country/region, order srch_destination_type_id to see most popular destination types
select user_location_country, user_location_region, srch_destination_type_id, count(srch_destination_type_id)
as srch_dest_id_type_cnt
from train
group by user_location_country, user_location_region, srch_destination_type_id
order by user_location_country ASC, user_location_region ASC, srch_dest_id_type_cnt DESC

# Count of # instances per user_location_country
select user_location_country,  count(user_location_country) as user_country_cnt from train
group by user_location_country
order by user_country_cnt DESC

# List hotel_markets and counts for each hotel_market given hotel_cluster
select hotel_cluster, hotel_market, count(hotel_cluster) as hotel_cluster_cnt from train
group by hotel_cluster, hotel_market
order by hotel_cluster ASC, hotel_cluster_cnt DESC

# List hotel_cluster & hotel_cluster_cnt given user_location_country and is_booking = 1 (i.e True)
select user_location_country, hotel_cluster, hotel_market, count(hotel_cluster) as hotel_cluster_cnt from train
where is_booking = 1
group by user_location_country, hotel_cluster, hotel_market
order by user_location_country ASC, hotel_cluster_cnt DESC, hotel_cluster ASC


# List cnt of hotel_cluster for each given set of user_location_region, user_location_country, srch_destination_type_id
# For when is_booking = 1 or 0
select  user_location_region, user_location_country, srch_destination_type_id, hotel_cluster, is_booking, count(hotel_cluster) as hotel_cluster_cnt
from train
group by user_location_region, user_location_country, srch_destination_type_id, is_booking, hotel_cluster
order by user_location_region asc, is_booking, hotel_cluster_cnt desc
