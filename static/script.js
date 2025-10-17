// Global state
let searchModal = null;
let searchInput = null;
let searchResults = null;
let outputDiv = null;

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    searchModal = document.getElementById('search-modal');
    searchInput = document.getElementById('search-input');
    searchResults = document.getElementById('search-results');
    outputDiv = document.getElementById('output');

    // Initialize terminal output on index page
    if (window.location.pathname === '/' || window.location.pathname === '/index.html') {
        initializeTerminal();
    }

    // Setup keyboard shortcuts
    setupKeyboardShortcuts();

    // Setup search input handler
    if (searchInput) {
        searchInput.addEventListener('input', handleSearchInput);
        searchInput.addEventListener('keydown', handleSearchKeydown);
    }

    // Setup upload form handler
    const uploadForm = document.getElementById('upload-form');
    if (uploadForm) {
        uploadForm.addEventListener('submit', handleUploadSubmit);
    }
});

// Initialize terminal with welcome message
function initializeTerminal() {
    const welcomeMessages = [
        '<span class="prompt">$</span> ./init_terminal.sh',
        '<span class="text-green">▶</span> Loading Previous Year Papers Database...',
        '<span class="text-green">✓</span> Database connected successfully',
        '<span class="text-green">✓</span> Search module loaded',
        '',
        '<span class="text-blue">Welcome to the Previous Year Papers Archive</span>',
        '',
        '<span class="text-yellow">Available Commands:</span>',
        '  • Press <span class="text-green">Ctrl+K</span> to search papers',
        '  • Type <span class="text-green">upload</span> in search to upload papers',
        '',
        '<span class="prompt">$</span> <span class="text-green">Ready for input...</span>'
    ];

    welcomeMessages.forEach((msg, index) => {
        setTimeout(() => {
            const line = document.createElement('div');
            line.className = 'terminal-line';
            line.innerHTML = msg;
            outputDiv.appendChild(line);
        }, index * 100);
    });
}

// Setup keyboard shortcuts
function setupKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Ctrl+K or Cmd+K to open search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            openSearchModal();
        }

        // Escape to close search
        if (e.key === 'Escape' && searchModal && !searchModal.classList.contains('hidden')) {
            closeSearchModal();
        }
    });
}

// Open search modal
function openSearchModal() {
    if (searchModal) {
        searchModal.classList.remove('hidden');
        searchInput.focus();
        searchInput.value = '';
        searchResults.innerHTML = '';
    }
}

// Close search modal
function closeSearchModal() {
    if (searchModal) {
        searchModal.classList.add('hidden');
        searchInput.value = '';
        searchResults.innerHTML = '';
    }
}

// Handle search input
async function handleSearchInput(e) {
    const query = e.target.value.trim();

    if (!query) {
        searchResults.innerHTML = '';
        return;
    }

    // Check if user typed "upload" (case-insensitive)
    if (query.toLowerCase() === 'upload') {
        searchResults.innerHTML = `
            <div class="search-result-item" style="border-color: #ffff00;">
                <div class="result-title" style="color: #ffff00;">📤 Upload Paper</div>
                <div class="result-meta">Navigate to upload page - Press Enter</div>
            </div>
        `;
        return;
    }

    // Show loading
    searchResults.innerHTML = '<div class="no-results"><span class="loading"></span> Searching...</div>';

    try {
        // Perform search
        const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        const results = await response.json();

        displaySearchResults(results);
    } catch (error) {
        console.error('Search error:', error);
        searchResults.innerHTML = '<div class="no-results text-red">Error performing search</div>';
    }
}

// Display search results
function displaySearchResults(results) {
    if (results.length === 0) {
        searchResults.innerHTML = '<div class="no-results">No papers found matching your query</div>';
        return;
    }

    searchResults.innerHTML = '';
    results.forEach(paper => {
        const item = document.createElement('div');
        item.className = 'search-result-item';
        item.innerHTML = `
            <div class="result-title">${paper.title}</div>
            <div class="result-meta">
                ${paper.subject} | ${paper.year} | ${paper.type}
                ${paper.tags.length > 0 ? ' | Tags: ' + paper.tags.join(', ') : ''}
            </div>
        `;
        item.addEventListener('click', () => selectPaper(paper));
        searchResults.appendChild(item);
    });
}

// Handle search keydown (Enter key)
function handleSearchKeydown(e) {
    if (e.key === 'Enter') {
        const query = e.target.value.trim();
        
        // Navigate to upload page if "upload" was typed
        if (query.toLowerCase() === 'upload') {
            window.location.href = '/upload';
        } else {
            // If there are search results, select the first one
            const firstResult = searchResults.querySelector('.search-result-item');
            if (firstResult) {
                firstResult.click();
            }
        }
    }
}

// Select a paper from search results
function selectPaper(paper) {
    closeSearchModal();
    
    // Add to terminal output
    const line = document.createElement('div');
    line.className = 'terminal-line';
    line.innerHTML = `
        <span class="prompt">$</span> view_paper "${paper.title}"<br>
        <span class="text-green">▶</span> Loading paper: <span class="text-blue">${paper.title}</span><br>
        <span class="text-yellow">Subject:</span> ${paper.subject}<br>
        <span class="text-yellow">Year:</span> ${paper.year}<br>
        <span class="text-yellow">Type:</span> ${paper.type}<br>
        <span class="text-yellow">Tags:</span> ${paper.tags.join(', ')}<br>
        <span class="text-green">✓</span> Paper details retrieved
    `;
    outputDiv.appendChild(line);
    
    // Scroll to bottom
    window.scrollTo(0, document.body.scrollHeight);
}

// Handle upload form submission
async function handleUploadSubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const formData = new FormData(form);
    const statusDiv = document.getElementById('upload-status');
    
    // Show loading
    statusDiv.className = '';
    statusDiv.innerHTML = '<span class="loading"></span> Uploading paper...';
    
    try {
        const response = await fetch('/api/upload', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (result.success) {
            statusDiv.className = 'success';
            statusDiv.innerHTML = `
                <span class="text-green">✓</span> Paper uploaded successfully!<br>
                <strong>Title:</strong> ${result.paper.title}<br>
                <strong>ID:</strong> ${result.paper.id}<br>
                <br>
                <span class="text-yellow">Note:</span> This paper will now appear in search results.
            `;
            
            // Add to terminal output
            const line = document.createElement('div');
            line.className = 'terminal-line';
            line.innerHTML = `
                <span class="prompt">$</span> upload_complete<br>
                <span class="text-green">✓</span> Paper "${result.paper.title}" added to database<br>
                <span class="text-green">✓</span> ID: ${result.paper.id}
            `;
            outputDiv.appendChild(line);
            
            // Clear form
            form.reset();
            
            // Scroll to status
            statusDiv.scrollIntoView({ behavior: 'smooth' });
        } else {
            throw new Error(result.error || 'Upload failed');
        }
    } catch (error) {
        console.error('Upload error:', error);
        statusDiv.className = 'error';
        statusDiv.innerHTML = `
            <span class="text-red">✗</span> Upload failed: ${error.message}
        `;
    }
}
