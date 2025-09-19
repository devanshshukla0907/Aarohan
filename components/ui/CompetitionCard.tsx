import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

interface CompetitionCardProps {
  name: string;
  location: string;
  startDate: string;
  endDate: string;
}

const CompetitionCard: React.FC<CompetitionCardProps> = ({ name, location, startDate, endDate }) => {
  return (
    <View style={styles.card}>
      <Text style={styles.title}>{name}</Text>
      <Text>{location}</Text>
      <Text>{startDate} - {endDate}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  card: {
    padding: 12,
    margin: 10,
    backgroundColor: '#f7f7f7',
    borderRadius: 6,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 3,
  },
  title: {
    fontWeight: 'bold',
    fontSize: 18,
  },
});

export default CompetitionCard;