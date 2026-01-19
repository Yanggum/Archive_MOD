# 주포안정기를 추가하기 위해 다음과 같은 변경사항을 적용함.

## 또한 모듈 파일에서 주포안정기 모듈에 대해 tank_BA_stabilizer_module 카테고리를 사용하도록 변경하고 GFX 파일에서 이미지를 추가한 후, 기존 특수 모듈의 아이콘을 변경함 (기존 특수 모듈이 주포안정기 아이콘을 사용하는 이유)

```

관련 파일:
common\units\equipment\tank_chassis.txt
common\units\equipment\modules\00_tank_modules.txt
common\units\equipment\modules\00_tank_modules_2.txt
interface\replace\BA_module.gfx

	light_tank_chassis = {
		year = 1922
		is_archetype = yes
		is_buildable = no

		can_be_produced = {
			if = {
				limit = {
					has_dlc = "Arms Against Tyranny"
				}
				NOT = {
					has_idea = BUL_army_restrictions_aat
				}
			}
			else = {
				NOT = {
					has_idea = BUL_army_restrictions
				}
			}
		}

		picture = archetype_light_tank_equipment
		type = armor
		group_by = archetype
		interface_category = interface_category_armor
		priority = 2000

		

		module_slots = {			

			turret_type_slot = { #Turrets must go at the top
				required = yes
				allowed_module_categories = {
					tank_light_turret_type
				}
			}
			
			main_armament_slot = {
				required = yes
				allowed_module_categories = {
					tank_small_main_armament
					tank_flamethrower
				}
			}
			
			suspension_type_slot = {
				required = yes
				allowed_module_categories = {
					tank_suspension_type
					tank_non_tracked_suspension_type
				}
			}

			armor_type_slot = {
				required = yes
				allowed_module_categories = {
					tank_armor_type
				}
			}

			engine_type_slot = {
				required = yes
				allowed_module_categories = {
					tank_engine_type
				}
			}

			special_type_slot_1 = {
				required = no
				allowed_module_categories = {
					tank_special_module
					tank_radio_module
					tank_secondary_turret
				}
			}

			special_type_slot_2 = {
				required = no
				allowed_module_categories = {
					tank_special_module
					tank_radio_module
					tank_secondary_turret
				}
			}

			special_type_slot_3 = {
				required = no
				allowed_module_categories = {
					tank_special_module
					tank_radio_module
					tank_secondary_turret
				}
			}

			special_type_slot_4 = {
				required = no
				allowed_module_categories = {
					tank_special_module
					tank_radio_module
					tank_secondary_turret
				}
			}
			
		}
		module_count_limit = {
			module = sloped_armor
			count < 2
		}	
		module_count_limit = {
			category = tank_radio_module
			count < 2
		}
		module_count_limit = {
			category = tank_secondary_turret
			count < 2
		}
		module_count_limit = {
			module = amphibious_drive
			count < 2
		}

		module_count_limit = {
			module = wet_ammo_storage
			count < 2
		}

		module_count_limit = {
			module = squeezebore_adaptor
			count < 2
		}

		module_count_limit = {
			module = armor_skirts
			count < 2
		}

		module_count_limit = {
			module = dozer_blade
			count < 2
		}

		module_count_limit = {
			module = easy_maintenance
			count < 2
		}
		module_count_limit = {
			module = auto_loader
			count < 2
		}
		module_count_limit = {
			module = stabilizer
			count < 2
		}
		default_modules = {
			main_armament_slot = empty
			turret_type_slot = tank_light_one_man_tank_turret
			suspension_type_slot = tank_bogie_suspension
			armor_type_slot = tank_riveted_armor
			engine_type_slot = tank_gasoline_engine
		}

		fuel_consumption = 0
		maximum_speed = 4
		build_cost_ic = 2
		reliability = 0.8
		hardness = 0.8
		armor_value = 10
		resources = {
			steel = 1
		}

		lend_lease_cost = 10

		manpower = 2

	}

	light_tank_chassis = {
		year = 1922
		is_archetype = yes
		is_buildable = no

		can_be_produced = {
			if = {
				limit = {
					has_dlc = "Arms Against Tyranny"
				}
				NOT = {
					has_idea = BUL_army_restrictions_aat
				}
			}
			else = {
				NOT = {
					has_idea = BUL_army_restrictions
				}
			}
		}

		picture = archetype_light_tank_equipment
		type = armor
		group_by = archetype
		interface_category = interface_category_armor
		priority = 2000

		

		module_slots = {			

			turret_type_slot = { #Turrets must go at the top
				required = yes
				allowed_module_categories = {
					tank_light_turret_type
				}
			}
			
			main_armament_slot = {
				required = yes
				allowed_module_categories = {
					tank_small_main_armament
					tank_flamethrower
				}
			}
			
			suspension_type_slot = {
				required = yes
				allowed_module_categories = {
					tank_suspension_type
					tank_non_tracked_suspension_type
				}
			}

			armor_type_slot = {
				required = yes
				allowed_module_categories = {
					tank_armor_type
				}
			}

			engine_type_slot = {
				required = yes
				allowed_module_categories = {
					tank_engine_type
				}
			}

			special_type_slot_1 = {
				required = no
				allowed_module_categories = {
					tank_special_module
					tank_BA_stabilizer_module
					tank_radio_module
					tank_secondary_turret
				}
			}

			special_type_slot_2 = {
				required = no
				allowed_module_categories = {
					tank_special_module
					tank_BA_stabilizer_module
					tank_radio_module
					tank_secondary_turret
				}
			}

			special_type_slot_3 = {
				required = no
				allowed_module_categories = {
					tank_special_module
					tank_BA_stabilizer_module
					tank_radio_module
					tank_secondary_turret
				}
			}

			special_type_slot_4 = {
				required = no
				allowed_module_categories = {
					tank_special_module
					tank_BA_stabilizer_module
					tank_radio_module
					tank_secondary_turret
				}
			}
			
		}
		module_count_limit = {
			module = sloped_armor
			count < 2
		}	
		module_count_limit = {
			category = tank_radio_module
			count < 2
		}
		module_count_limit = {
			category = tank_secondary_turret
			count < 2
		}
		module_count_limit = {
			module = amphibious_drive
			count < 2
		}

		module_count_limit = {
			module = wet_ammo_storage
			count < 2
		}

		module_count_limit = {
			module = squeezebore_adaptor
			count < 2
		}

		module_count_limit = {
			module = armor_skirts
			count < 2
		}

		module_count_limit = {
			module = dozer_blade
			count < 2
		}

		module_count_limit = {
			module = easy_maintenance
			count < 2
		}
		module_count_limit = {
			module = auto_loader
			count < 2
		}
		module_count_limit = {
			category = tank_BA_stabilizer_module
			count < 2
		}
		default_modules = {
			main_armament_slot = empty
			turret_type_slot = tank_light_one_man_tank_turret
			suspension_type_slot = tank_bogie_suspension
			armor_type_slot = tank_riveted_armor
			engine_type_slot = tank_gasoline_engine
		}

		fuel_consumption = 0
		maximum_speed = 4
		build_cost_ic = 2
		reliability = 0.8
		hardness = 0.8
		armor_value = 10
		resources = {
			steel = 1
		}

		lend_lease_cost = 10

		manpower = 2

	}

```

# 키보토스식 열차 추가를 위해 다음과 같은 파일을 수정함
## common\units\equipment\trains.txt

```
	# BA trains
	train_equipment_4 = {
		year = 1936

		archetype = train_equipment
		parent = train_equipment_3
		priority = 40

		armor_value = 360 # HP = BASE_TRAIN_HP + armor_value
		air_attack = 36

		build_cost_ic = 125
		resources = {
			steel = 2
			pyroxenes = 2
		}
	}
```