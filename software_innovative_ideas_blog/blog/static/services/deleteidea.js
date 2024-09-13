function setTopic(topic, topicID) {
    document.getElementById("selectedtopic").innerText = topic
    document.getElementById("topic").value = topicID;
    return topic
}

function getSelectedTopic() {
    var topic = document.getElementById("selectedtopic").innerHTML;
    return topic;
}

function getUserId() {
    var userid = document.getElementById("id").innerHTML;
    return userid;
}

function deleteIdea(ideaID, topicID, currenttopic) {

    document.getElementById('ideaID').value = ideaID;
    document.getElementById('topicID').value = topicID;
    document.getElementById('currenttopic').value = currenttopic;

    var form = document.getElementById('deleteidea');
    form.appendChild(document.getElementById('ideaID'))
    form.appendChild(document.getElementById('idea'))
    form.appendChild(document.getElementById('topic'))

    form.submit();
}
