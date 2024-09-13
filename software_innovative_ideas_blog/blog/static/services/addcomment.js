
function setComment(userid) {
    document.getElementById("form_comment").value = document.getElementById("comment").value;
}

function editComment(ideaID, userID, comment, commentID) {
    document.getElementById('ideaID').value = ideaID
    document.getElementById('userID').value = userID
    document.getElementById('comment').value = comment
    document.getElementById('commentID').value = commentID

    var form = document.getElementById('editcomment');

    form.appendChild(document.getElementById('ideaID'))
    form.appendChild(document.getElementById('userID')) 
    form.appendChild(document.getElementById('comment'))
    form.appendChild(document.getElementById('commentID'))

    form.submit();
}

function deleteComment(ideaID, userID, comment, commentID) {

    document.getElementById('ideaID').value = ideaID
    document.getElementById('userID').value = userID
    document.getElementById('comment').value = comment
    document.getElementById('commentID').value = commentID

    var form = document.getElementById('deletecomment');

    form.appendChild(document.getElementById('ideaID'))
    form.appendChild(document.getElementById('userID'))
    form.appendChild(document.getElementById('comment'))
    form.appendChild(document.getElementById('commentID'))

    form.submit();
}