


function liked(e){
    const likeable = document.getElementById('likeable');
    const { likes, dislikes } = likeable.dataset;


    const likeShow = document.getElementById('like-show');
    const dislikeShow = document.getElementById('dislike-show');

    if(+likeShow.innerText == likes) {
        likeShow.innerText = +likes + 1;
        $("#like-icon").toggleClass('far fas');
        if(+dislikeShow.innerText !== +dislikes) {
            dislikeShow.innerText = dislikes;
            $("#dislike-icon").toggleClass('fas far');
        }
        return;
    }
    if(+likeShow.innerText !== likes) {
        $("#like-icon").toggleClass('fas far');
        likeShow.innerText = likes;
        return;
    }
}

function disliked(e){
    const likeable = document.getElementById('likeable');
    const { likes, dislikes } = likeable.dataset;


    const dislikeShow = document.getElementById('dislike-show');
    const likeShow = document.getElementById('like-show');

    if(+dislikeShow.innerText == dislikes) {
        dislikeShow.innerText = +dislikes + 1;
        $("#dislike-icon").toggleClass('far fas');

        if(+likeShow.innerText !== +likes) {
            $("#like-icon").toggleClass('fas far');
            likeShow.innerText = likes;
            return;
        }

        return;
    }
    if(+dislikeShow.innerText !== dislikes) {
        $("#dislike-icon").toggleClass('fas far');
        dislikeShow.innerText = dislikes;
        return;
    }
}

function initialize(){
    const likeable = document.getElementById('likeable');
    const { likes, dislikes } = likeable.dataset;

    console.log(likes, dislikes)

    const likeShow = document.getElementById('like-show');
    const dislikeShow = document.getElementById('dislike-show');

    likeShow.innerText = likes;
    dislikeShow.innerText = dislikes;
}

initialize();
