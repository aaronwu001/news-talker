import React, { useState } from 'react';
import { View, TextInput, Text, TouchableOpacity, StyleSheet, Image } from 'react-native';
import { Link } from 'expo-router';

export default function SignUpScreen() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSignUp = () => {
    console.log('Sign Up:', email, password);
  };

  return (
    <View style={styles.container}>
      <Image 
        source={require('../assets/images/logo.png')}
        style={styles.logo}
      />
      
      <Text style={styles.headerTitle}>Register</Text>
      <Text style={styles.subtitle}>Get past the noise.</Text>

      <TextInput
        style={styles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
        autoCapitalize="none"
      />
      
      <TextInput
        style={styles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
        autoCapitalize="none"
      />

      <TextInput
        style={styles.input}
        placeholder="Confirm Password"
        value={confirmPassword}
        onChangeText={setConfirmPassword}
        secureTextEntry
        autoCapitalize="none"
      />
      
      <TouchableOpacity style={styles.button} onPress={handleSignUp}>
        <Text style={styles.buttonText}>Sign Up</Text>
      </TouchableOpacity>

      <View style={styles.linksContainer}>
        <Link href="../" asChild>
          <TouchableOpacity>
            <Text style={styles.link}>Already have an account? Login</Text>
          </TouchableOpacity>
        </Link>
      </View>
    </View>
  );
}
const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      padding: 20,
      backgroundColor: '#f5f5f5',
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
      color: '#000',
      marginBottom: 8,
    },
    subtitle: {
      fontSize: 16,
      textAlign: 'center',
      color: '#000',
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
    button: {
      backgroundColor: '#007bff',
      padding: 15,
      borderRadius: 8,
      alignItems: 'center',
      marginBottom: 20,
    },
    buttonText: {
      color: '#fff',
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