import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, ActivityIndicator, Image } from 'react-native';
import { useState, useMemo, useEffect, useReducer } from 'react';
import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';
import Drawer from './routes/DrawerNav';
import Auth from './routes/AuthStackNav';
import FavorSettingStack from './routes/FavorSettingStack';
import { AuthContext } from './content/AuthContext';
import { API_URL } from '@env';
import * as SecureStore from 'expo-secure-store';
import { LogBox } from 'react-native';
LogBox.ignoreLogs(['Warning: ...']); // Ignore log notification by message
LogBox.ignoreAllLogs();//Ignore all log notifications

export default function App() {
  const initialLoginState = {
    isLoading: true,
    userId: null,
    userToken: null,
    everWroteFavor: false,
  };

  const authReducer = (state, action) => {
    //狀態
    switch (action.type) {
      case 'LOADING':
        return {
          ...state,
          userId: action.id,
          userToken: action.token,
          isLoading: false,
          everWroteFavor: true,
        };
      case 'LOGIN':
        return {
          ...state,
          userId: action.id,
          userToken: action.token,
          isLoading: false,
          everWroteFavor: true,
        };
      case 'LOGOUT':
        return {
          ...state,
          userId: null,
          userToken: null,
          isLoading: false,
        };
      case 'SIGNUP':
        return {
          ...state,
          userId: action.id,
          userToken: action.token,
          isLoading: false,
          everWroteFavor: false,
        };
    }
  };

  const [Authstate, dispatch] = useReducer(authReducer, initialLoginState);

  const authContext = useMemo(() => ({
    login: async (account, password) => {
      //api call
      const requestOption = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          account: account,
          password: password,
        }),
      };
      let userToken, userId, res;
      try {
        res = await fetch(`${API_URL}/user/login`, requestOption).then((r) =>
          r.json()
        );
        userId = res.uid;
        userToken = res.token;
      } catch (e) {
        console.error(e);
      }
      if (userId && userToken) {
        await SecureStore.setItemAsync('auth-token', userToken);
        await SecureStore.setItemAsync('user-id', userId);
      }
      setTimeout(() => {
        dispatch({
          type: 'LOGIN',
          id: userId,
          token: userToken,
        });
      }, 280);
      return res;
    },
    logout: async () => {
      await SecureStore.deleteItemAsync('auth-token');
      await SecureStore.deleteItemAsync('user-id');
      dispatch({ type: 'LOGOUT' });
    },
    signup: async (name, account, password) => {
      //api call
      const requestOption = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: name,
          account: account,
          password: password,
        }),
      };
      let userToken, userId;
      try {
        const res = await fetch(`${API_URL}/user/register`, requestOption);
        const json = await res.json();
        userId = json.info._id;
        userToken = json.token;
      } catch (e) {
        console.error(e);
      }
      if (userId && userToken) {
        await SecureStore.setItemAsync('auth-token', userToken);
        await SecureStore.setItemAsync('user-id', userId);
      }
      dispatch({
        type: 'SIGNUP',
        id: userId,
        token: userToken,
      });
    },
  }));
  useEffect(() => {
    const fetchUser = async () => {
      let token = await SecureStore.getItemAsync('auth-token');
      let userId = null;
      const requestOption = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          token: token,
        }),
      };
      const response = await fetch(
        `${API_URL}/user/isTokenValid`,
        requestOption
      ).then((res) => res.json());
      if (response) {
        userId = await SecureStore.getItemAsync('user-id');
      } else {
        await SecureStore.deleteItemAsync('auth-token');
        await SecureStore.deleteItemAsync('user-id');
        token = null;
      }
      setTimeout(() => {
        dispatch({
          type: 'LOADING',
          token: token,
          id: userId,
        });
      }, 1000);
    };
    fetchUser();
  }, []);
  if (Authstate.isLoading) {
    return (
      <View style={styles.container}>
        <Image source={require('./assets/logo.jpg')} style={styles.photo} />
        {/*<ActivityIndicator size="small" />*/}
      </View>
    );
  }
  if (Authstate.userToken == null) {
    return (
      <AuthContext.Provider value={authContext}>
        <StatusBar style="auto" />
        <NavigationContainer>
          <Auth />
        </NavigationContainer>
      </AuthContext.Provider>
    );
  }
  if (!Authstate.everWroteFavor) {
    return (
      <AuthContext.Provider value={authContext}>
        <StatusBar style="auto" />
        <NavigationContainer>
          <FavorSettingStack />
        </NavigationContainer>
      </AuthContext.Provider>
    );
  } else {
    return (
      <AuthContext.Provider value={authContext}>
        <StatusBar style="auto" />
        <NavigationContainer>
          <Drawer />
        </NavigationContainer>
      </AuthContext.Provider>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#EFFAFF',
  },
  photo: {
    width: 200,
    height: 200,
  },
});
