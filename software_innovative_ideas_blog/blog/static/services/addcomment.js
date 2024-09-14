
function setComment(ideaID, userid, authorID) {

    document.getElementById('ideaID').value = ideaID
    document.getElementById('authorID').value = authorID 
    document.getElementById('form_comment').value = document.getElementById('textcomment').value

    var form = document.getElementById('addcomment');

    form.appendChild(document.getElementById('ideaID'))
    form.appendChild(document.getElementById('authorID')) 
    form.appendChild(document.getElementById('form_comment'))

    form.submit();
}

function editComment(ideaID, userID, authorID, comment, commentID) {
    document.getElementById('ideaID').value = ideaID
    document.getElementById('userID').value = userID
    document.getElementById('userID').value = userID
    document.getElementById('authorID').value = authorID
    document.getElementById('comment').value = comment
    document.getElementById('commentID').value = commentID

    var form = document.getElementById('editcomment');

    form.appendChild(document.getElementById('ideaID'))
    form.appendChild(document.getElementById('userID')) 
    form.appendChild(document.getElementById('comment'))
    form.appendChild(document.getElementById('commentID'))

    form.submit();
}

function deleteComment(ideaID, userID, authorID, comment, commentID) {

    document.getElementById('ideaID').value = ideaID
    document.getElementById('userID').value = userID
    document.getElementById('authorID').value = authorID
    document.getElementById('comment').value = comment
    document.getElementById('commentID').value = commentID

    var form = document.getElementById('deletecomment');

    form.appendChild(document.getElementById('ideaID'))
    form.appendChild(document.getElementById('userID'))
    form.appendChild(document.getElementById('authorID'))
    form.appendChild(document.getElementById('comment'))
    form.appendChild(document.getElementById('commentID'))

    form.submit();
}

function addComment(idea, ideaID, userID, commentID) {
    document.getElementById('ideaID').value = ideaID
    document.getElementById('userID').value = userID
    document.getElementById('commentID').value = commentID
    document.getElementById('authorID').value = userID
    document.getElementById('form_comment').value = document.getElementById('comment').value
    var form = document.getElementById('editcomment');

    form.appendChild(document.getElementById('ideaID'))
    form.appendChild(document.getElementById('userID'))
    form.appendChild(document.getElementById('commentID'))
    form.appendChild(document.getElementById('authorID'))
    form.appendChild(document.getElementById('comment'))

    //form.submit();
}