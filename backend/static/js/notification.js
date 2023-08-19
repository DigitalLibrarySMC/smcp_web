
document.addEventListener('DOMContentLoaded', function() {
  function showNotification(message, type) {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    notificationContainer.appendChild(notification);
  
    setTimeout(() => {
      notification.remove();
    }, 5000);
  }
  
  const notificationContainer = document.getElementById('notification-container');
  const notifications = [
    { message: 'Welcome to our website!', type: 'success' },
    { message: 'There was an error processing your request.', type: 'error' },
    // Add more notifications as needed
  ];
  
  let currentIndex = 0;
  
  function showNextNotification() {
    const { message, type } = notifications[currentIndex];
    showNotification(message, type);
    currentIndex = (currentIndex + 1) % notifications.length;
  }
  
  // Show the first notification
  showNextNotification();
  
  // Schedule to show the next notification after 5 seconds
  setInterval(showNextNotification, 5000);
  
});
