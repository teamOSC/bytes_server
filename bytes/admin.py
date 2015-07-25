'''
class ModelBAdmin(admin.ModelAdmin):

    def modelA_Codes(self, inst):
        return ','.join([b.code for b in inst.modela_set.all()])

    list_display = ('name', 'modelA_Codes')

class HotelAdmin(admin.ModelAdmin):

    list_display = ['name', 'rating', 'logo', 'rooms', 'hotel_id']


class AppliancesAdmin(admin.ModelAdmin):

    list_display = ['room_number', 'appliance_id', 'on', 'name']


class RoomAdmin(admin.ModelAdmin):

    list_display = ['hotel_id', 'user', 'room_server', 'room_number', 'type_id', 'type_name', 'appliances']



class HotelRoomsAdmin(admin.ModelAdmin):

    list_display = ['type_id', 'type_name', 'total', 'available', 'rate', 'beds']


admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelRooms, HotelRoomsAdmin)
admin.site.register(Appliances, AppliancesAdmin)
admin.site.register(Room, RoomAdmin)
'''