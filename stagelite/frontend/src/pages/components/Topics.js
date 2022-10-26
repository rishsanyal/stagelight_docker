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
      chosenTopic: null,
      currentTopic: null,

    }
  }

  componentWillMount() {
    this.props.getTopicsList();
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevProps.topics !== this.props.topics) {
      console.log(this.props.topics);
      this.setState({
        topics: this.props.topics,
        currentTopic: this.props.topics[0],
      })
    }
  }

  render() {
    return (
      <center>
        <h1>Topics</h1>
        {console.log(this.state.topics)}
      </center>
    )
  }
}

const mapStateToProps = (state) => {
  return {
      topics: state
      //Non-action functions can go here
  };
};

export default connect(
  mapStateToProps,
  {
      getTopicsList
  })
(Topics);