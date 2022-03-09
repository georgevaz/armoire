from attr import has
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from . import forms

from .models import User, Piece, Outfit, PieceToOutfit


# Create your views here.
def index(request):
    return render(request, "Armoire_app/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("mycloset"))
        else:
            return render(request, "Armoire_app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "Armoire_app/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "Armoire_app/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "Armoire_app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("mycloset"))
    else:
        return render(request, "Armoire_app/register.html")


@login_required
def add_piece(request):
    if request.method == "POST":
        form = forms.PieceForm(request.POST, request.FILES)
        if form.is_valid():
            piece = form.save(commit=False)
            piece.user_id = request.user
            piece.save()
            return HttpResponseRedirect("mycloset")
    else:
        form = forms.PieceForm()
    return render(request, "Armoire_app/addpiece.html", {
        'form': form
    })


@login_required
def my_closet(request):
    if request.method == "POST":
        form = forms.PieceForm(request.POST, request.FILES)
        if form.is_valid():
            piece = form.save(commit=False)
            piece.user_id = request.user
            piece.save()
        else:
            outfit = Outfit()
            outfit.user_id = request.user
            outfit.name = request.POST["outfit-name"]
            outfit.save()
            return HttpResponseRedirect(reverse("outfit", kwargs={'outfit_id': outfit.id}))
        return HttpResponseRedirect("mycloset")

    else:
        pieces = Piece.objects.filter(user_id=request.user)
        tops = Piece.objects.filter(user_id=request.user, category="Top")
        bottoms = Piece.objects.filter(user_id=request.user, category="Bottom")
        onepieces = Piece.objects.filter(user_id=request.user, category="Onepiece")
        shoes = Piece.objects.filter(user_id=request.user, category="Shoes")
        accessories = Piece.objects.filter(user_id=request.user, category="Accessories")
        outfits = Outfit.objects.filter(user_id=request.user)
        outfit_pieces = {}
        for outfit in outfits:
            pieces_in_outfits = pieces_in_outfit(outfit.id)
            single_pieces = []
            i = 0
            for outfit_piece in pieces_in_outfits:
                if i < 4:
                    piece = Piece.objects.get(id=outfit_piece.id)
                    single_pieces.append(piece)
                    i += 1
            
            outfit_pieces[outfit] = single_pieces
        form = forms.PieceForm()
        return render(request, "Armoire_app/mycloset.html", {
            "pieces": pieces,
            "tops": tops,
            "bottoms": bottoms,
            "onepieces": onepieces,
            "shoes": shoes,
            "accessories": accessories,
            "outfits": outfits,
            "outfitpieces": outfit_pieces,
            "form": form
        })


@login_required
def outfit(request, outfit_id):
    pieces = pieces_in_outfit(outfit_id)
    return render(request, "Armoire_app/outfit.html", {
        "outfit": Outfit.objects.get(id=outfit_id),
        "pieces": pieces,
        "all": Piece.objects.filter(user_id=request.user),
        "tops": Piece.objects.filter(user_id=request.user, category="Top"),
        "bottoms": Piece.objects.filter(user_id=request.user, category="Bottom"),
        "onepieces": Piece.objects.filter(user_id=request.user, category="Onepiece"),
        "shoes": Piece.objects.filter(user_id=request.user, category="Shoes"),
        "accessories": Piece.objects.filter(user_id=request.user, category="Accessories")
    })


@login_required
def piecetooutfit(request, piece_id, outfit_id):
    if request.user.is_authenticated:
        in_outfit = False
        # Find the piece
        piece = Piece.objects.get(id=piece_id)
        # Find all pieces in outfit
        pieces = pieces_in_outfit(outfit_id)
        outfit = Outfit.objects.get(id=outfit_id)
        # Check if piece is in list of pieces
        for i in pieces:
            if i == piece:
                in_outfit = True

        # If clicked and it is in outfit, remove piece
        if in_outfit:
            in_outfit = False
            PieceToOutfit.objects.get(outfit_id=outfit, piece_id=piece).delete()
        # Otherwise add piece
        else:
            in_outfit = True
            piece_to_outfit = PieceToOutfit()
            piece_to_outfit.outfit_id = outfit
            piece_to_outfit.piece_id = piece
            piece_to_outfit.save()
        return JsonResponse({
            'in_outfit': in_outfit
        })


def pieces_in_outfit(outfit_id):
    outfit = Outfit.objects.get(id=outfit_id)
    pieces_in_outfit = PieceToOutfit.objects.filter(outfit_id=outfit)
    pieces = []
    for piece in pieces_in_outfit:
        pieces.append(Piece.objects.get(id=piece.piece_id.id))
    return pieces

@login_required
def deletepiece(request, piece_id):
    if request.user.is_authenticated:
        outfits_with_piece = PieceToOutfit.objects.filter(piece_id=piece_id)
        if outfits_with_piece:
            for outfit in outfits_with_piece:
                outfit.delete()
        piece = Piece.objects.get(id=piece_id)
        piece.delete()

    return JsonResponse({
        "deleted": True
    })

@login_required
def deleteoutfit(request, outfit_id):
    if request.user.is_authenticated:
        pieces_in_outfit = PieceToOutfit.objects.filter(outfit_id=outfit_id)
        if pieces_in_outfit:
            for outfit_piece in pieces_in_outfit:
                outfit_piece.delete()
        outfit = Outfit.objects.get(id=outfit_id)
        outfit.delete()
    return JsonResponse({
        "deleted": True
    })