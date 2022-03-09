document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll(".piece").forEach(piece => {
        piece.addEventListener("click", function () {
            piece_id = piece.id;
            outfit_id = document.querySelector(".outfit-id").id;
            fetch(`/piecetooutfit/${piece_id}&${outfit_id}`)
                .then(response => response.json())
                .then(data => {
                    let pieces;
                    pieces = document.querySelectorAll(`.piece-${piece_id}`)
                    if (data.in_outfit === true) {
                        pieces.forEach(i => {
                            i.classList.add('selected');
                            i.classList.remove('not-selected');
                        });
                    } else {
                        pieces.forEach(i => {
                            i.classList.remove('selected');
                            i.classList.add('not-selected');
                        });
                    };

                });

        })
    })
});

function show_piece_form() {
    document.querySelector('#outfits-pieces').style.display = 'none';
    document.querySelector('#piece-form').style.display = 'block';
};
function show_outfit_form() {
    document.querySelector('#outfits-pieces').style.display = 'none';
    document.querySelector('#outfit-form').style.display = 'block';
};
function show_delete_field(){
    document.querySelector('#outfits-pieces').style.display = 'none';
    document.querySelector('#delete-pieces').style.display = 'block';
};
function show_delete_outfit(){
    document.querySelector('#outfits-pieces').style.display = 'none';
    document.querySelector('#delete-outfits').style.display = 'block';
};
function hide_forms() {
    document.querySelector('#outfits-pieces').style.display = 'block';
    document.querySelector('#piece-form').style.display = 'none';
    document.querySelector('#outfit-form').style.display = 'none';
};

function show_all_pieces() {
    document.querySelector('.outfit').style.display = 'none';
    document.querySelector('.add-piece').style.display = 'none';
    document.querySelector('.back-to-outfit').style.display = 'block';
    document.querySelector('#all-pieces').style.display = 'block';
};

function show_all() {
    document.querySelector('#tops').style.display = 'none';
    document.querySelector('#bottoms').style.display = 'none';
    document.querySelector('#onepieces').style.display = 'none';
    document.querySelector('#shoes').style.display = 'none';
    document.querySelector('#accessories').style.display = 'none';
    document.querySelector('#all').style.display = 'block';
    change_buttons("All");
};
function show_tops() {
    document.querySelector('#tops').style.display = 'block';
    document.querySelector('#bottoms').style.display = 'none';
    document.querySelector('#onepieces').style.display = 'none';
    document.querySelector('#shoes').style.display = 'none';
    document.querySelector('#accessories').style.display = 'none';
    document.querySelector('#all').style.display = 'none';
    change_buttons("Tops");
};
function show_bottoms() {
    document.querySelector('#tops').style.display = 'none';
    document.querySelector('#bottoms').style.display = 'block';
    document.querySelector('#onepieces').style.display = 'none';
    document.querySelector('#shoes').style.display = 'none';
    document.querySelector('#accessories').style.display = 'none';
    document.querySelector('#all').style.display = 'none';
    change_buttons("Bottoms");
};
function show_onepieces() {
    document.querySelector('#tops').style.display = 'none';
    document.querySelector('#bottoms').style.display = 'none';
    document.querySelector('#onepieces').style.display = 'block';
    document.querySelector('#shoes').style.display = 'none';
    document.querySelector('#accessories').style.display = 'none';
    document.querySelector('#all').style.display = 'none';
    change_buttons("Onepieces");
};
function show_shoes() {
    document.querySelector('#tops').style.display = 'none';
    document.querySelector('#bottoms').style.display = 'none';
    document.querySelector('#onepieces').style.display = 'none';
    document.querySelector('#shoes').style.display = 'block';
    document.querySelector('#accessories').style.display = 'none';
    document.querySelector('#all').style.display = 'none';
    change_buttons("Shoes");
};
function show_accessories() {
    document.querySelector('#tops').style.display = 'none';
    document.querySelector('#bottoms').style.display = 'none';
    document.querySelector('#onepieces').style.display = 'none';
    document.querySelector('#shoes').style.display = 'none';
    document.querySelector('#accessories').style.display = 'block';
    document.querySelector('#all').style.display = 'none';
    change_buttons("Accessories");
};
function change_buttons(category){
    document.querySelectorAll('.category-button').forEach(button => {
        if (button.innerHTML == category){
            button.classList.add('btn-primary-small');
            button.classList.remove('btn-secondary-small');
        } else {
            button.classList.remove('btn-primary-small');
            button.classList.add('btn-secondary-small');
        }
    });
}

function delete_entry(piece_id, button){
    fetch(`/deletepiece/${piece_id}`)
    let entries = document.querySelectorAll(`#entry-${piece_id}`);
    button.onclick = null;
    entries.forEach(element => {
        element.classList.add("deleted");
    });
    
    setTimeout(() => {
        entries.forEach(element => {
            element.remove();
        });

    }, 900 );

};

function delete_outfit(outfit_id, button){
    fetch(`/deleteoutfit/${outfit_id}`)
    let outfit = document.querySelector(`#outfit-${outfit_id}`)
    button.onclick = null;

    outfit.classList.add("deleted")
    setTimeout(() => {
        outfit.remove();

    }, 900 );
};