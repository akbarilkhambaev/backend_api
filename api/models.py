from django.db import models

class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="subcategories",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    name = models.CharField("Название подкатегории", max_length=100)

    def __str__(self):
        return f"{self.category.name} → {self.name}"


class Service(models.Model):
    subcategory = models.ForeignKey(
        Subcategory,
        related_name="services",
        on_delete=models.CASCADE,
        verbose_name="Подкатегория",
    )
    name = models.CharField("Название услуги", max_length=200)
    description = models.TextField("Описание услуги", blank=True)

    def __str__(self):
        return f"{self.subcategory.name} → {self.name}"

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
