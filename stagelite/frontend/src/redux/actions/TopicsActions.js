import {FETCH_TOPICS} from '../ActionTypes'

import axios, * as others from 'axios';

import Cookies from 'js-cookie';

export function getTopicsList(){

    // let myValue;
    // function currentloginid() {
    //     return fetch('http://0.0.0.0:8000/trial_topics/', {
    //         method: 'GET',
    //     })
    //     .then(function(response) {
    //         return response.json();
    //     })
    //     .then(function(data) {
    //         var userid = data;
    //         myValue = userid
    //         return userid;
    //     })}
    // myValue = currentloginid().then(value => {

    // })
    // axios.get('http://0.0.0.0:8000/trial_topics/').then(response => {
    //     myValue = response.data;
    //     return response.data;
    // });

    const username = Cookies.get('username');

    return fetch(
        'http://127.0.0.1:8000/topics/topics_list?username='+username
    ).then(response => response.json()).then(data => {
        console.log(data['topics']);
        return data
    })
    // console.log(myValue);
    // return myValue;
}

export function getSpecificTopicsList(topicId){

    return fetch(
        'http://127.0.0.1:8000/topics/topics_list/' + topicId + "/"
    ).then(response => response.json()).then(data => {
        console.log(data['topics']);
        return data
    })
}

export function voteTopic(topicId, voteType){

    const username = Cookies.get('username');

    return fetch(
        "http://127.0.0.1:8000/topics/voteTopic/?type="+voteType+"&id="+topicId+"&username="+username,
    )
}

export function getUserSubmission(username, topicId){
        return fetch(
            "http://127.0.0.1:8000/topics/submission/?username="+username+"&topicId="+topicId,
        ).then(response => response.json()).then(data => {
            console.log(data);
            return data['userEntry']
        }
    )
}