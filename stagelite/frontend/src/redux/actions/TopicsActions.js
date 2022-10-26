import {FETCH_TOPICS} from '../ActionTypes'

import axios, * as others from 'axios';

export function getTopicsList(){

    let myValue;
    function currentloginid() {
        return fetch('http://0.0.0.0:8000/trial_topics/', {
            method: 'GET',
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            var userid = data;
            myValue = userid
            return userid;
        })}
    // myValue = currentloginid().then(value => {

    // })
    axios.get('http://0.0.0.0:8000/trial_topics/').then(response => {
        myValue = response.data;
    });

    console.log(myValue);
    return {
        type: FETCH_TOPICS,
        payload: myValue
    }
}