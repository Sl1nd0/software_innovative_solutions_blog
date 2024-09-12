
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

