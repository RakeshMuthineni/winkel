from django.contrib import admin
from Store.models import product,Variation,ReviewRating,ProductGallery
import admin_thumbnails
# Register your models here.


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class productAdmin(admin.ModelAdmin):
    prepopulated_fields  = {'slug':('product_name',)}
    list_display=['product_name','price','stock','category','modified_date','is_avilable']
    inlines = [ProductGalleryInline]

admin.site.register(product,productAdmin)

class VariationAdmin(admin.ModelAdmin):

    list_display=('product','variation_category','variation_value','is_active')
    list_filter = ('product','variation_category','variation_value')
    list_editable = ('is_active',)





admin.site.register(Variation,VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
