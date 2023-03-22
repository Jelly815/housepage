SELECT *
FROM `ex_record_items` items,`ex_record_items_stay` stay
WHERE items.id = stay.record_items_id and
      items.user_id = 'm8456fba48ba8c14bdd683e92c7414dc8' AND
      stay.type_key != 'stay_time' AND
      items.`last_time` BETWEEN (NOW() - INTERVAL 180 DAY) AND NOW()
ORDER by items.main_id