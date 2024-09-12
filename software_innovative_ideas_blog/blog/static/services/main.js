
//async function logout() {
//    try {
//        const response = await red("/login/");
//        if (!response.ok) {
//            throw new Error("Network response was not OK");
//        }
//    } catch (error) {
//        console.error("There was a problem with your fetch request: ", error);
//    }
//}

//function addComment(userid, ideaid, idea) {
//   //alert(userid + " " + ideaid + " " + idea)
//    let dto = {
//        "userID": userid,
//        "ideaID": ideaid,
//        "idea":idea
//    }
//}

function setTopic(topic, topicID) {
    document.getElementById("selectedtopic").innerText = topic
    document.getElementById("topic").value = topicID;
    return topic
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
