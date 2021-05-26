from django.contrib import admin
from django.utils.html import format_html

from constructor import models as ConstructorModels
from django import forms


@admin.register(ConstructorModels.CategoryComponents)
class CategoryComponentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.CategoryComponents._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Category._meta.fields] + ['show_components']
    ordering = ['id']
    search_fields = ('name',)

    def show_components(self, obj):
        return ",".join([a.key for a in obj.components.all()])


@admin.register(ConstructorModels.Body)
class ProductBodyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Body._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Sleeve)
class ProductSleeveAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Sleeve._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Collar)
class ProductCollarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Collar._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Hood)
class HoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Hood._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Cuff)
class ProductCuffAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Cuff._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Pocket)
class PocketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Pocket._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.SleevePocket)
class SleevePocketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.SleevePocket._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.PantsPocket)
class PantsPocketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.PantsPocket._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Zip)
class ZipAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Zip._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Strap)
class StrapAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Strap._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.StrapBuckle)
class StrapBuckleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.StrapBuckle._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Rope)
class RopeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Rope._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Hem)
class ProductHemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Hem._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Lining)
class LiningAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Lining._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Bottom)
class BottomAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Bottom._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Pants)
class PentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Pants._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Color._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.FabricCategory)
class FabricAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.FabricCategory._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Fabric)
class FabricAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Fabric._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.SizeFieldModel)
class SizeFieldModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.SizeFieldModel._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.ProductSizeModel)
class ProductSizeModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.ProductSizeModel._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.ProductDesign)
class ProductDesignAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'front_image_tag', 'back_image_tag']
    ordering = ['id']
    search_fields = ('name',)

    def front_image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.front_view.url))

    def back_image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.back_view.url))
