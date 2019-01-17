CREATE OR REPLACE VIEW ex_user_record_view AS
SELECT `record`.`id` AS `record_id`,`record`.`user_id` AS `user_id`,`record`.`area` AS `area`,`record`.`price` AS `price`,`record`.`ping` AS `ping`,`record`.`style` AS `style`,`record`.`type` AS `type`,`record`.`times` AS `record_times`,`items`.`main_id`,`items`.`times` AS `items_times`,`items`.`click_map` AS `click_map`,`items`.`add_favorite` AS `add_favorite`,`items`.`last_time` AS `last_time`,`items_stay`.`stay_time` AS `item_stay_time`,`items_map`.`stay_time` AS `map_stay_time` from (`ex_record` `record` join ((`ex_record_items` `items`

LEFT JOIN `ex_record_items_stay` `items_stay`
ON((`items_stay`.`record_items_id` = `items`.`id`)))

LEFT JOIN `ex_record_items_map` `items_map`
ON((`items_map`.`record_items_id` = `items`.`id`))))

WHERE (`record`.`id` = `items`.`record_id` AND record.`times` > 1 AND `items_stay`.`stay_time` > 5 AND `items`.`last_time` >= (NOW() - INTERVAL 180 DAY))