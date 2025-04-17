import React, { useState } from 'react';
import { View, TextInput, Text, TouchableOpacity, StyleSheet, Image, ImageBackground } from 'react-native';
import { Link } from 'expo-router';
import { useForm, Controller } from 'react-hook-form';
import * as zod from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';

const authSchema = zod.object({
  email: zod.string().email('Invalid email address'),
  password: zod.string().min(6, 'Password must be at least 6 characters long'),
})

export default function Auth() {
  const {control, handleSubmit, formState} = useForm({
    resolver: zodResolver(authSchema),
    defaultValues: {
      email: '',
      password: '',
    }
  })

  const signIn = (data: zod.infer<typeof authSchema>) => {
    console.log(data);
  };

  const signUp = (data: zod.infer<typeof authSchema>) => {
    console.log(data);
  };

  return (
    <ImageBackground source={{
      uri: 'https://images.pexels.com/photos/312418/pexels-photo-312418.jpeg?cs=srgb&dl=pexels-chevanon-312418.jpg&fm=jpg'
    }}
    style={styles.backgroundImage}
    >
      <View style={styles.overlay}>
        <View style={styles.container}>
          <Image 
            source={require('../assets/images/logo.png')}
            style={styles.logo}
          />
          
          <Text style={styles.headerTitle}>Welcome to NewsBrew</Text>
          <Text style={styles.subtitle}>Please authenticate to continue.</Text>
          
          <Controller
            control={control}
            name='email'
            render={({
              field: {value, onChange, onBlur},
              fieldState: {error}
            }) => (
              <>
                <TextInput
                  style={styles.input}
                  placeholder="Email"
                  value={value}
                  onChangeText={onChange}
                  onBlur={onBlur}
                  placeholderTextColor={'#aaa'}
                  editable={!formState.isSubmitting}
                  autoCapitalize="none"
                />
                {error && <Text style={{color: 'red'}}>{error.message}</Text>}
              </>
            )}
          ></Controller>
          
          <Controller
            control={control}
            name='password'
            render={({
              field: {value, onChange, onBlur},
              fieldState: {error}
            }) => (
              <>
                <TextInput
                  style={styles.input}
                  placeholder="Password"
                  value={value}
                  onChangeText={onChange}
                  onBlur={onBlur}
                  placeholderTextColor={'#aaa'}
                  secureTextEntry
                  editable={!formState.isSubmitting}
                  autoCapitalize="none"
                />
                {error && <Text style={{color: 'red'}}>{error.message}</Text>}
              </>
            )}
          ></Controller>
          
          <View style={styles.buttonsContainer}>
            <Link href="./home" asChild>
              <TouchableOpacity
                style={styles.button}
                disabled={formState.isSubmitting}>
                <Text style={styles.buttonText}>Sign In</Text>
              </TouchableOpacity>
            </Link>
            
            <TouchableOpacity
              style={styles.outlineButton}
              onPress={handleSubmit(signUp)}
              disabled={formState.isSubmitting}>
              <Text style={styles.outlineButtonText}>Sign Up</Text>
            </TouchableOpacity>
          </View>
        </View>
      </View>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 20,
  },
  backgroundImage: {
    flex: 1,
    resizeMode: 'cover',
    justifyContent: 'center',
    alignItems: 'center',
  },
  overlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
  },
  logo: {
    width: 120,
    height: 120,
    alignSelf: 'center',
    marginBottom: 20,
    resizeMode: 'contain',
  },
  headerTitle: {
    fontSize: 32,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#FFF',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    textAlign: 'center',
    color: '#FFF',
    marginBottom: 40,
  },
  input: {
    height: 50,
    borderColor: '#ddd',
    borderWidth: 1,
    marginBottom: 20,
    padding: 15,
    borderRadius: 8,
    backgroundColor: '#fff',
  },
  buttonsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 10,
  },
  button: {
    backgroundColor: '#007bff',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
    flex: 0.48,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  outlineButton: {
    backgroundColor: 'transparent',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
    borderWidth: 2,
    borderColor: '#007bff',
    flex: 0.48,
  },
  outlineButtonText: {
    color: '#007bff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  linksContainer: {
    alignItems: 'center',
    gap: 15,
  },
  link: {
    color: '#007bff',
    fontSize: 14,
  },
});