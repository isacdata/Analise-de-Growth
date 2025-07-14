
WITH visitors_info as (
select
s.visitor_id,
v.user_id,
v.first_visit_date,
IFNULL(REPLACE(s.utm_source, ",", ";"),  "Organic") as channel,
i.date_registered,
MIN(p.date_purchased) as first_purchase_date,
i.first_watch_date
from 
front_visitors as v
inner join 
front_sessions as s on v.visitor_id = s.visitor_id
left join
student_info as i on v.user_id = i.user_id
left join
student_purchases as p on v.user_id = p.user_id
where
v.first_visit_date >="2022-07-01"
and
(v.first_visit_date < i.date_registered or i.date_registered is null)
group by
s.visitor_id, 
        v.user_id, 
        v.first_visit_date, 
        channel, 
        i.date_registered, 
        i.first_watch_date
),

count_total as (
select 
count(*) as count_visitors,
first_visit_date,
channel
from visitors_info
group by first_visit_date, channel
),

count_free as (
select 
count(*) as count_free,
first_visit_date,
channel
from visitors_info
where
date_registered is not null 
and (first_purchase_date is null or timestampdiff(minute, date_registered, first_purchase_date)>30)
group by first_visit_date, channel
),

count_watched as (
select 
count(*) as count_watched,
first_visit_date,
channel
from visitors_info
where
first_watch_date is not null and (first_purchase_date is null or first_watch_date < first_purchase_date)
group by first_visit_date, channel
),

count_paid as (
select 
count(*) as count_paid,
first_visit_date,
channel
from visitors_info
where
first_purchase_date is not null
group by first_visit_date, channel
)

select
t.first_visit_date,
t.channel,
t.count_visitors,
IFNULL(f.count_free, 0) as count_free,
IFNULL(w.count_watched, 0) as count_watched,
IFNULL(p.count_paid, 0) as count_paid
from 
count_total as t
left join
count_free as f on t.first_visit_date = f.first_visit_date and t.channel = f.channel
left join
count_watched as w on t.first_visit_date = w.first_visit_date and t.channel = w.channel
left join
count_paid as p on t.first_visit_date = p.first_visit_date and t.channel = p.channel
order by first_visit_date, count_visitors desc limit 1000;