SELECT a.user_id,a.area,a.price,a.ping,a.style,a.type,a.times,b.main_id,b.times,b.click_map,b.add_favorite
FROM `ex_record` a,`ex_record_items` b

WHERE a.user_id = b.user_id AND a.id = b.record_id AND
		a.user = 'mca3907edc888d46215b3a35c294e73fa'
ORDER BY a.`user_id` ASC