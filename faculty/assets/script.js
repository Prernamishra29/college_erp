// Sample script for dynamic interactions
document.addEventListener("DOMContentLoaded", () => {
    // Add Course Modal
    const addCourseBtn = document.getElementById('add-course-btn');
    const addCourseModal = document.getElementById('add-course-modal');
    const closeCourseModal = document.getElementById('close-course-modal');
  
    // Show Add Course Modal
    addCourseBtn.addEventListener("click", () => {
      addCourseModal.classList.remove("hidden");
    });
  
    // Close Add Course Modal
    closeCourseModal.addEventListener("click", () => {
      addCourseModal.classList.add("hidden");
    });
  
    // Additional modals for Attendance, Grading can be added similarly
  });
  