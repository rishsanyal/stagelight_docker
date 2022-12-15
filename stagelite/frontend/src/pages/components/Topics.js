import React, { Component } from 'react';
import { useEffect, useState } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import { getTopicsList, getList } from '../../redux/actions/TopicsActions';
import TopicDisplay from './TopicDisplay';

function Topics(props) {

  const [topics, setTopics] = useState([]);

  useEffect(() => {
    let mounted = true;
    getTopicsList().then(items => {
      if(mounted) {
        setTopics(items['topics'])
        }
    })

    return () => mounted = false;
  }, []);



  return (
    <div>
    <h1>
    </h1>

      {topics.map((topic) => (
        <div>
          {/* {topic.title} */}
          <TopicDisplay title={topic.title} upvotes={topic.upvotes} downvotes={topic.downvotes} id={topic.id}/>
        </div>
      ))}

    </div>
  )
}

Topics.propTypes = {}

export default Topics;
