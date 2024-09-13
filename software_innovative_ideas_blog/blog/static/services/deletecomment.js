
function setComment(userid) {
    document.getElementById("form_comment").value = document.getElementById("comment").value;
}

function deleteComment(idea, ideaID, userID, commentID) {
    document.getElementById('ideaID').value = ideaID
    document.getElementById('userID').value = userID
    document.getElementById('commentID').value = commentID
    document.getElementById('authorID').value = userID

    var form = document.getElementById('editcomment');

    form.appendChild(document.getElementById('ideaID'))
    form.appendChild(document.getElementById('userID')) 
    form.appendChild(document.getElementById('commentID')) 
    form.appendChild(document.getElementById('authorID'))
    form.appendChild(document.getElementById('comment'))

    form.submit();
}