import React, { useState } from 'react';
import { View, Text, ScrollView, Pressable, Modal, TextInput, StyleSheet, Image } from 'react-native';

interface NewsItem {
  id: number;
  title: string;
  content: string;
  readTime: string;
  imageUrl: string;
}

interface NewsCardProps {
  item: NewsItem;
  onPress: () => void;
}

const newsItems: NewsItem[] = [
  {
    id: 1,
    title: 'Global Climate Summit Kicks Off',
    content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce varius justo id turpis finibus, vel laoreet nunc feugiat. Integer ut sem vitae nisi tincidunt laoreet. Vivamus eget tincidunt odio, at tincidunt est. Sed consectetur augue vel magna facilisis, in faucibus nulla tempus.',
    readTime: '4 minute read',
    imageUrl: 'https://images.pexels.com/photos/2559941/pexels-photo-2559941.jpeg',
  },
  {
    id: 2,
    title: 'Nvidia Unveils AI Breakthrough',
    content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce varius justo id turpis finibus, vel laoreet nunc feugiat. Integer ut sem vitae nisi tincidunt laoreet. Vivamus eget tincidunt odio, at tincidunt est. Sed consectetur augue vel magna facilisis, in faucibus nulla tempus.',
    readTime: '6 minute read',
    imageUrl: 'https://images.pexels.com/photos/1714208/pexels-photo-1714208.jpeg',
  },
  {
    id: 3,
    title: 'New Renewable Energy Record Set',
    content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce varius justo id turpis finibus, vel laoreet nunc feugiat. Integer ut sem vitae nisi tincidunt laoreet. Vivamus eget tincidunt odio, at tincidunt est. Sed consectetur augue vel magna facilisis, in faucibus nulla tempus.',
    readTime: '3 minute read',
    imageUrl: 'https://images.pexels.com/photos/414837/pexels-photo-414837.jpeg',
  },
  {
    id: 4,
    title: 'Global Tech Conference Highlights',
    content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce varius justo id turpis finibus, vel laoreet nunc feugiat. Integer ut sem vitae nisi tincidunt laoreet. Vivamus eget tincidunt odio, at tincidunt est. Sed consectetur augue vel magna facilisis, in faucibus nulla tempus.',
    readTime: '5 minute read',
    imageUrl: 'https://images.pexels.com/photos/2582937/pexels-photo-2582937.jpeg',
  },
  {
    id: 5,
    title: 'Space Tourism Mission Announced',
    content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce varius justo id turpis finibus, vel laoreet nunc feugiat. Integer ut sem vitae nisi tincidunt laoreet. Vivamus eget tincidunt odio, at tincidunt est. Sed consectetur augue vel magna facilisis, in faucibus nulla tempus.',
    readTime: '7 minute read',
    imageUrl: 'https://images.pexels.com/photos/41162/moon-landing-apollo-11-nasa-buzz-aldrin-41162.jpeg',
  },
];

const NewsCard: React.FC<NewsCardProps> = ({ item, onPress }) => (
  <Pressable style={styles.card} onPress={onPress}>
    <View style={styles.cardContent}>
      <Image 
        source={{ uri: item.imageUrl }}
        style={styles.cardImage}
      />
      <View style={styles.cardTextContainer}>
        <Text style={styles.cardTitle}>{item.title}</Text>
        <Text style={styles.readTime}>{item.readTime}</Text>
      </View>
    </View>
  </Pressable>
);

const NewsDetailScreen: React.FC<{ item: NewsItem; onBack: () => void }> = ({ item, onBack }) => (
  <View style={styles.container}>
    <ScrollView contentContainerStyle={styles.detailScrollContent}>
      <Pressable style={styles.backButton} onPress={onBack}>
        <Text style={styles.backButtonText}>← Back</Text>
      </Pressable>
      <Image 
        source={{ uri: item.imageUrl }}
        style={styles.detailImage}
      />
      <Text style={styles.detailTitle}>{item.title}</Text>
      <Text style={styles.content}>{item.content}</Text>
    </ScrollView>
  </View>
);

const AskAIModal: React.FC<{ visible: boolean; onClose: () => void }> = ({ visible, onClose }) => {
  const [query, setQuery] = useState('');

  return (
    <Modal visible={visible} transparent>
      <View style={styles.modalOverlay}>
        <View style={styles.modalContent}>
          <TextInput
            style={styles.input}
            placeholder="Ask AI..."
            value={query}
            onChangeText={setQuery}
          />
          <Pressable style={styles.submitButton} onPress={onClose}>
            <Text style={styles.buttonText}>Submit</Text>
          </Pressable>
        </View>
      </View>
    </Modal>
  );
};

const NavBar: React.FC<{ onAskAI: () => void }> = ({ onAskAI }) => (
  <View style={styles.navBar}>
    <Pressable style={styles.navButton}>
      <Text>Home</Text>
    </Pressable>
    <Pressable style={styles.navButton}>
      <Text>Browse</Text>
    </Pressable>
    <Pressable style={styles.navButton} onPress={onAskAI}>
      <Text>Ask AI</Text>
    </Pressable>
    <Pressable style={styles.navButton}>
      <Text>Settings</Text>
    </Pressable>
  </View>
);

export default function App() {
  const [currentScreen, setCurrentScreen] = useState<'main' | 'detail'>('main');
  const [selectedItem, setSelectedItem] = useState<NewsItem | null>(null);
  const [isModalVisible, setIsModalVisible] = useState(false);

  const handleCardPress = (item: NewsItem) => {
    setSelectedItem(item);
    setCurrentScreen('detail');
  };

  return (
    <View style={styles.container}>
      {currentScreen === 'main' ? (
        <View style={styles.container}>
          <ScrollView contentContainerStyle={styles.scrollContent}>
            <View style={styles.header}>
              <Image 
                          source={require('../assets/images/logo.png')}
                          style={styles.logo}
                        />
              <Text style={styles.title}>Hello!</Text>
              <Text style={styles.subtitle}>The news, brewed fresh.</Text>
            </View>
            {newsItems.map((item) => (
              <NewsCard
                key={item.id}
                item={item}
                onPress={() => handleCardPress(item)}
              />
            ))}
          </ScrollView>
          <NavBar onAskAI={() => setIsModalVisible(true)} />
        </View>
      ) : (
        selectedItem && (
          <NewsDetailScreen
            item={selectedItem}
            onBack={() => setCurrentScreen('main')}
          />
        )
      )}

      <AskAIModal visible={isModalVisible} onClose={() => setIsModalVisible(false)} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  scrollContent: {
    paddingTop: 50, // Added padding at the top
  },
  detailScrollContent: {
    paddingTop: 50, // Adding padding at the top of the detail view
  },
  header: {
    padding: 16,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 8,
    alignContent: 'center',
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    alignContent: 'center',
    textAlign: 'center',
  },
  card: {
    backgroundColor: '#fff',
    borderRadius: 8,
    padding: 12,
    margin: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  cardContent: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  cardImage: {
    width: 80,
    height: 80,
    borderRadius: 6,
    marginRight: 12,
  },
  cardTextContainer: {
    flex: 1,
  },
  logo: {
    width: 40,
    height: 40,
    alignSelf: 'center',
    marginBottom: 20,
    resizeMode: 'contain',
  },
  cardTitle: {
    fontSize: 16,
    fontWeight: '600',
    marginBottom: 8,
  },
  readTime: {
    fontSize: 14,
    color: '#666',
  },
  detailTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    margin: 16,
  },
  detailImage: {
    width: '100%',
    height: 200,
    resizeMode: 'cover',
  },
  content: {
    fontSize: 16,
    lineHeight: 24,
    marginHorizontal: 16,
    marginBottom: 16,
  },
  navBar: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    paddingVertical: 16,
    borderTopWidth: 1,
    borderTopColor: '#eee',
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.5)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modalContent: {
    backgroundColor: 'white',
    padding: 20,
    borderRadius: 8,
    width: '80%',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 4,
    padding: 12,
    marginBottom: 16,
  },
  submitButton: {
    backgroundColor: '#007AFF',
    padding: 12,
    borderRadius: 4,
    alignItems: 'center',
  },
  buttonText: {
    color: 'white',
    fontWeight: '600',
  },
  backButton: {
    padding: 16,
  },
  backButtonText: {
    fontSize: 16,
    color: '#007AFF',
  },
  navButton: {
    padding: 8,
  },
});