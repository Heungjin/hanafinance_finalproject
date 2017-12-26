<template>
  <div id="app">
    <navigation/>
    <top/>
    <about-section/>
    <call-action-section/>
    <service-section/>
    <contact-section/>
    <list-product/>
    <testimoials-section/>
    <age-state/>
    <port-grid-section/>
    <portfolio-section/>
    <bottom/>

    <portfolio-modal-ex1/>
  </div>
</template>

<script>

import AboutSection from '@/components/AboutSection'
import callActionSection from '@/components/callActionSection'
import ContactSection from '@/components/ContactSection'
import Bottom from '@/components/Footer'
import Top from '@/components/Header'
import Navigation from '@/components/Navigation'
import PortfolioModalEx1 from '@/components/PortfolioModalEx1'  
import portfolioSection from '@/components/portfolioSection'
import PortGridSection from '@/components/PortGridSection'
import ServiceSection from '@/components/ServiceSection'
import TestimoialsSection from '@/components/TestimoialsSection'
import ListProduct from './components/ListProduct'
import ageState from './components/ageState'

export default {
  name: 'app',
  components: {
AboutSection, 
callActionSection, 
ContactSection,
Bottom,
Top,
Navigation,
PortfolioModalEx1, 
portfolioSection,
PortGridSection,
ServiceSection,
TestimoialsSection,
ListProduct,
ageState

  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
