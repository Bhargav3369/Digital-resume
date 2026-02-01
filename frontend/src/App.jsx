import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import AboutMe from './pages/AboutMe';
import Research from './pages/Research';
import Projects from './pages/Projects';
import Contact from './pages/Contact';
import usePageTracking from './services/usePageTracking';

function PageTracker() {
    usePageTracking();
    return null;
}

function App() {
    return (
        <Router>
            <div className="app-container">
                <PageTracker />
                <Navbar />
                <main className="content">
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/about" element={<AboutMe />} />
                        <Route path="/research" element={<Research />} />
                        <Route path="/projects" element={<Projects />} />
                        <Route path="/contact" element={<Contact />} />
                    </Routes>
                </main>
                <Footer />
            </div>
        </Router>
    );
}

export default App;
