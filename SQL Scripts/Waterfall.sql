SELECT
user_id,
subscription_id,
case 
when subscription_type = 0 then "Monthly"
when subscription_type = 1 then "Quarter"
when subscription_type = 2 then "Annual"
end as plan,
subscription_status as status,
cast(date_start as date) as sub_start,
cast(date_deactivated as date) as sub_end
from student_subscriptions
where
subscription_type != 3
order by
user_id,
date_start