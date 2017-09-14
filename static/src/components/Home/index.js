/* eslint camelcase: 0, no-underscore-dangle: 0 */

import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import Paper from 'material-ui/Paper';
import PaypalButton from '../Payment/PaypalButton';
import BraintreeButton from '../Payment/BraintreeButton';
import StripeButton from '../Payment/StripeButton';

// import * as actionCreators from '../actions/auth';
// import { validateEmail } from '../utils/misc';

// function mapStateToProps(state) {
//     return {
//         isAuthenticating: state.auth.isAuthenticating,
//         statusText: state.auth.statusText,
//     };
// }

// function mapDispatchToProps(dispatch) {
//     return bindActionCreators(actionCreators, dispatch);
// }


const style = {
    marginTop: 50,
    paddingBottom: 50,
    paddingTop: 25,
    width: '100%',
    textAlign: 'center',
    display: 'inline-block',
};

// @connect(mapStateToProps, mapDispatchToProps)
export default class HomeView extends React.Component {

    constructor(props) {
        super(props);
        // const redirectRoute = '/login';
        this.state = {
            name:'',
            phone: '',
            items: [{
              'name': 'test_item',
              'price': '5.00',
              'currency': 'USD',
              'quantity': 1
            }],
            amount: {
              'total': '5.00',
              'currency': 'USD'
            }
        };
    }

    changeValue(e, type) {
        const value = e.target.value;
        const next_state = {};
        next_state[type] = value;
        this.setState(next_state);
    }

    _handleKeyPress(e) {
        if (e.key === 'Enter') {
            if (!this.state.disabled) {
                this.pay(e);
            }
        }
    }

    // pay(e) {
    //     e.preventDefault();
    //     this.props.loginUser(this.state.email, this.state.password, this.state.redirectTo);
    // }

    render() {
        return (
            <div className="col-md-6 col-md-offset-3" onKeyPress={(e) => this._handleKeyPress(e)}>
                <Paper style={style}>
                    <form role="form">
                        <div className="text-center">
                            <h2>Payment Demo</h2>

                            <div className="col-md-12">
                                <TextField
                                  hintText="Name"
                                  floatingLabelText="Name"
                                  type="text"
                                  onChange={(e) => this.changeValue(e, 'name')}
                                />
                            </div>
                            <div className="col-md-12">
                                <TextField
                                  hintText="Phone"
                                  floatingLabelText="Phone"
                                  type="text"
                                  onChange={(e) => this.changeValue(e, 'phone')}
                                />
                            </div>

                            <PaypalButton disabled={false} data={this.state}/>
                            <BraintreeButton disabled={false} data={this.state}/>
                            <StripeButton disabled={false} data={this.state}/>

                        </div>
                    </form>
                </Paper>

            </div>
        );

    }
}
