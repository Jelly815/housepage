CREATE OR REPLACE VIEW ex_user_record_view_not AS
SELECT `record`.`id` AS `record_id`,`record`.`user_id` AS `user_id`,`record`.`area` AS `area`,
`record`.`price` AS `price`,`record`.`ping` AS `ping`,`record`.`style` AS `style`,
`record`.`type` AS `type`,`record`.`times` AS `record_times`,`items`.`main_id`,
`items`.`times` AS `items_times`,`items`.`click_map` AS `click_map`,
`items`.`add_favorite` AS `add_favorite`,`items`.`last_time` AS `last_time`,
`items_stay`.`type_value` AS `item_stay_time`
FROM `ex_record` `record`,`ex_record_items` `items`

LEFT JOIN `ex_record_items_stay` `items_stay`
ON `items_stay`.`record_items_id` = `items`.`id` AND `items_stay`.`type_key`='stay_time'

WHERE `record`.`id` = `items`.`record_id` AND `items`.`times` = 1 AND
	`items`.`add_favorite` = 0 AND `items_stay`.`type_value` > 5 AND
	(SELECT COUNT(`id`) FROM `ex_main` WHERE `is_closed` = 0 AND `id` = `items`.`main_id`) > 0
