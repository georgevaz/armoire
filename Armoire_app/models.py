from pickle import REDUCE
from sre_parse import CATEGORIES
from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass


class Piece(models.Model):
    TOP = 'Top'
    BOTTOM = 'Bottom'
    ONEPIECE = 'Onepiece'
    SHOES = 'Shoes'
    ACCESSORIES = 'Accessories'
    CATEGORIES = [
        (TOP, 'Top'),
        (BOTTOM, 'Bottom'),
        (ONEPIECE, 'Onepiece'),
        (SHOES, 'Shoes'),
        (ACCESSORIES, 'Accessories')
    ]

    RED = 'Red'
    PINK = 'Pink'
    ORANGE = 'Orange'
    YELLOW = 'Yellow'
    GREEN = 'Green'
    BLUE = 'Blue'
    INDIGO = 'Indigo'
    VIOLET = 'Violet'
    BEIGE = 'Beige'
    TAN = "Tan"
    WHITE = 'White'
    BLACK = 'Black'
    BROWN = 'Brown'
    GRAY = 'Gray'
    MULTI = 'Multi-Color'
    COLORS = [
        (RED, 'Red'),
        (PINK, 'Pink'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (BEIGE, 'Beige'),
        (TAN, 'Tan'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
        (BROWN, 'Brown'),
        (GRAY, 'Gray'),
        (MULTI, 'Multi-Color'),
    ]

    user_id = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="piece")
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to="img/", default="")
    category = models.CharField(max_length=32, choices=CATEGORIES, default=TOP)
    color = models.CharField(max_length=32, choices=COLORS, default=WHITE)
    season = models.CharField(max_length=64)
    style = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} : {self.user_id}'s {self.name}"


class Outfit(models.Model):
    user_id = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="outfit")
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} : {self.user_id}'s {self.name}"


class PieceToOutfit(models.Model):
    piece_id = models.ForeignKey(
        "Piece", on_delete=models.CASCADE, related_name="piece_to_outfit")
    outfit_id = models.ForeignKey(
        "Outfit", on_delete=models.CASCADE, related_name="piece_to_outfit")

    def __str__(self):
        return f"{self.id} : {self.piece_id} in outfit {self.outfit_id}"
