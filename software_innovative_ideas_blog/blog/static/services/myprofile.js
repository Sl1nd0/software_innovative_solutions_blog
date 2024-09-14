
function setTopic(topic, topicID) {
    document.getElementById("selectedtopic").innerText = topic
    document.getElementById("topic").value = topicID;
    return topic
}

function filterByTopic(topicID) {
    document.getElementById('topicID').value = topicID
    var form = document.getElementById('filterbytopic');
    form.appendChild(document.getElementById('topicID'))

    form.submit();
}

function gotoListLikes(test, userid) {
    document.getElementById('ideaID').value = test.ideaID;
    document.getElementById('idea').value = test.idea; 
    document.getElementById('userID').value = test.userID;

    var form = document.getElementById('listlikes');
    form.appendChild(document.getElementById('ideaID'))
    form.appendChild(document.getElementById('userID'))
    form.appendChild(document.getElementById('idea'))

    form.submit();
}

function gotoListComments(test, userid) {
    document.getElementById('ideaID').value = test.ideaID;
    document.getElementById('idea').value = test.idea;
    document.getElementById('userID').value = test.userID;

    var form = document.getElementById('listcomments');
    form.appendChild(document.getElementById('ideaID'))
    form.appendChild(document.getElementById('userID'))
    form.appendChild(document.getElementById('idea'))

    form.submit();
}

function editPost(idea, topic, userid)
{
    document.getElementById('ideaID').value = idea.ideaID;
    document.getElementById('idea').value = idea.idea;
    document.getElementById('topic').value = topic;
    document.getElementById('topicID').value = idea.topicID;

    var form = document.getElementById('editidea');
    form.appendChild(document.getElementById('ideaID'))
    form.appendChild(document.getElementById('idea'))
    form.appendChild(document.getElementById('topic'))

    form.submit();
}

function deletePost(idea, topic, userid) {
    document.getElementById('ideaID').value = idea.ideaID;
    document.getElementById('idea').value = idea.idea;
    document.getElementById('topic').value = topic;

    var form = document.getElementById('deleteidea');
    form.appendChild(document.getElementById('ideaID'))
    form.appendChild(document.getElementById('idea'))
    form.appendChild(document.getElementById('topic'))

    form.submit();
}
