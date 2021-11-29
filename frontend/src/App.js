import * as React from 'react';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import CountriesTable from './components/CountriesTable'


export default function App() {
  return (
    <Container>
      <Typography variant="h3" component="h1" sx={{ textAlign: 'center' }}>
        Climate Change
      </Typography>
      <Typography variant="h4" component="h4" sx={{ textAlign: 'center' }}>
        The Countries with most temperature changes
      </Typography>
      <Box sx={{ my: 4 }}>
       <CountriesTable></CountriesTable>
      </Box>
    </Container>
  );
}