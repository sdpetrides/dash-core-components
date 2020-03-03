/* global window:true */

import PropTypes from 'prop-types';

import React, {Component} from 'react';

import R from 'ramda';

/*
 * event polyfill for IE
 * https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent/CustomEvent
 */
function CustomEvent(event, params) {
    // eslint-disable-next-line no-param-reassign
    params = params || {
        bubbles: false,
        cancelable: false,
        // eslint-disable-next-line no-undefined
        detail: undefined,
    };
    const evt = document.createEvent('CustomEvent');
    evt.initCustomEvent(
        event,
        params.bubbles,
        params.cancelable,
        params.detail
    );
    return evt;
}
CustomEvent.prototype = window.Event.prototype;

export default class Pathname extends Component {
    constructor(props) {
        super(props);
        this.updateLocation = this.updateLocation.bind(this);
    }

    updateLocation(e) {
        // prevent anchor from updating location
        e.preventDefault();
        const {pathname, refresh} = this.props;
        const search = window.location.search
        const hash = window.location.hash
        const searchVal = R.type(search) !== 'Undefined' ? search : '';
        const hashVal = R.type(hash) !== 'Undefined' ? hash : '';
        if (refresh) {
            window.location.pathname = `${pathname}${searchVal}${hashVal}`;
        } else {
            window.history.pushState(
                {},
                '',
                `${pathname}${searchVal}${hashVal}`
            )
            window.dispatchEvent(new CustomEvent('onpushstate'));
        }
        // scroll back to top
        window.scrollTo(0, 0);
    }

    render() {
        const {className, style, id, pathname, loading_state} = this.props;
        /*
         * ideally, we would use cloneElement however
         * that doesn't work with dash's recursive
         * renderTree implementation for some reason
         */
        if (style !== undefined) {
          style.cursor = 'pointer';
        }
        return (
            <a
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }
                id={id}
                className={className}
                style={style}
                pathname={pathname}
                onClick={e => this.updateLocation(e)}
            >
                {this.props.children}
            </a>
        );
    }
}

Pathname.propTypes = {
    pathname: PropTypes.string,
    refresh: PropTypes.bool,
    className: PropTypes.string,
    style: PropTypes.object,
    id: PropTypes.string,
    children: PropTypes.node,
    /**
     * Object that holds the loading state object coming from dash-renderer
     */
    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string,
    }),
};

Pathname.defaultProps = {
    refresh: false,
};
