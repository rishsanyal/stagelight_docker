import {FETCH_TOPICS} from '../ActionTypes'

import axios, * as others from 'axios';

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

    return fetch(
        'http://0.0.0.0:8000/trial_topics/'
    ).then(response => response.json()).then(data => {
        console.log(data['topics']);
        return data
    })
    // console.log(myValue);
    // return myValue;
}

export function getSpecificTopicsList(topicId){

    return fetch(
        'http://localhost:8000/topics/topics_list/' + topicId + "/"
    ).then(response => response.json()).then(data => {
        console.log(data['topics']);
        return data
    })
}