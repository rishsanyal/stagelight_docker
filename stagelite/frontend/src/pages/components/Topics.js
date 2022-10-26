import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';


import { getTopicsList } from '../../redux/actions/TopicsActions';

class Topics extends Component {
  static propTypes = {
    prop: PropTypes
  }

  constructor(props) {
    super(props);
    console.log("HERE");
    this.state = {
      topics: [],
      topicsSet: false
    }
  }

  componentWillMount() {
    this.props.getTopicsList();
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevProps.topics !== this.props.topics) {
      this.setState({
        topics: this.props.topics
      })
    }
  }

  render() {
    return (
      <center>
        <h1>Topics</h1>
        {this.state.topics.map((topic) => (
            <div>
              <h3>{topic.topic}</h3>
              <p>{topic.description}</p>
            </div>
          ))}
      </center>
    )
  }
}

const mapStateToProps = (state) => {
  return {
      //Non-action functions can go here
  };
};

export default connect(
  mapStateToProps,
  {
      getTopicsList
  })
(Topics);