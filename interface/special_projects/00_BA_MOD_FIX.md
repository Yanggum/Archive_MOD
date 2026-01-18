# 변경 1
- scientist_roster.gui 내 specialization_sort_entry 가 밀려 보이는 문제 해결을 위한 덮어쓰기
``` //specialization_sort_entry

		buttonType = {
			name = "specialization_icon"
			position = { x = 95 y = 15 }
			spriteType = "GFX_raid_unit_icon_nuclear_raids"
			scale = 0.4
		}

--> 아래와 같이 값을 수정

		buttonType = {
			name = "specialization_icon"
			# /BA_MOD_FIX
			position = { x = 55 y = 15 }
			# BA_MOD_FIX/
			spriteType = "GFX_raid_unit_icon_nuclear_raids"
			scale = 0.4
		}
```