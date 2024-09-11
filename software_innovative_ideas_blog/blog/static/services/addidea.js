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
