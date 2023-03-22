SELECT `record`.`id` AS `record_id`,`record`.`user_id` AS `user_id`,
`record`.`area` AS `area`, `record`.`price` AS `price`,
`record`.`ping` AS `ping`,`record`.`style` AS `style`,
`record`.`type` AS `type`,`record`.`times` AS `record_times`,
`items`.`main_id`, `items`.`times` AS `items_times`,
`items`.`click_map` AS `click_map`, `items`.`add_favorite` AS `add_favorite`,
`items`.`last_time` AS `last_time`,
(	SELECT (SUM(`type_value`) / COUNT(`id`))
	FROM `ex_record_items_stay`
	WHERE 	`type_key`= 'stay_time' and
			`record_items_id` = `items`.`id`) AS `item_stay_time`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'age' and
			`record_items_id` = `items`.`id`) AS `item_age`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'area' and
			`record_items_id` = `items`.`id`) AS `item_area`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'around' and
			`record_items_id` = `items`.`id`) AS `item_around`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'builder' and
			`record_items_id` = `items`.`id`) AS `item_builder`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'community' and
			`record_items_id` = `items`.`id`) AS `item_community`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'status' and
			`record_items_id` = `items`.`id`) AS `item_status`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'direction' and
			`record_items_id` = `items`.`id`) AS `item_direction`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'type' and
			`record_items_id` = `items`.`id`) AS `item_type`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'floor' and
			`record_items_id` = `items`.`id`) AS `item_floor`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'parking' and
			`record_items_id` = `items`.`id`) AS `item_parking`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'room' and
			`record_items_id` = `items`.`id`) AS `item_room`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'price' and
			`record_items_id` = `items`.`id`) AS `item_price`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'unit' and
			`record_items_id` = `items`.`id`) AS `item_unit`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'fee' and
			`record_items_id` = `items`.`id`) AS `item_fee`,
(	SELECT `type_value` FROM `ex_record_items_stay`
	WHERE `type_key`= 'ping' and
			`record_items_id` = `items`.`id`) AS `item_ping`

FROM `ex_record` `record`,`ex_record_items` `items`
WHERE `record`.`id` = `items`.`record_id` AND
(`items`.`times` > 1 OR `items`.`add_favorite` = 1) AND
`items`.`last_time` >= (NOW() - INTERVAL 180 DAY) AND
(SELECT COUNT(`id`) FROM `ex_main` WHERE `id` = `items`.`main_id`) > 0