// The `dead_code` allow covers types and methods that are defined here but only
// exercised by the test suite. Once you implement everything and uncomment the
// demo code in main.rs, these warnings disappear naturally.
#![allow(dead_code)]

use std::collections::HashMap;

// ============================================================================
// TYPES: do not modify these definitions
// ============================================================================

pub struct Student {
    pub id: String,
    pub name: String,
    pub email: String,
    pub credits_earned: u16,
    pub grades: Vec<CourseGrade>,
}

#[derive(Debug, Clone, PartialEq)]
pub enum Grade {
    A,
    B,
    C,
    D,
    F,
}

#[derive(Debug, Clone)]
pub struct CourseGrade {
    pub course_code: String,
    pub course_name: String,
    pub credits: u16,
    pub grade: Grade,
}

pub struct StudentDatabase {
    students: HashMap<String, Student>,
}

// ============================================================================
// IMPLEMENTATIONS: replace every todo!() with a real implementation.
// When you do, remove the leading `_` from each parameter name.
// ============================================================================

impl Student {
    /// Creates a new student with the given id, name, and email.
    /// `credits_earned` starts at 0 and `grades` starts empty.
    pub fn new(id: String, name: String, email: String) -> Student {
        Student {
            id,
            name,
            email,
            credits_earned: 0,  // A new student has not earned credits yet.
            grades: Vec::new(), // Start with an empty list of course grades.
        }
    }

    /// Returns a string describing the student's class standing based on credits:
    ///   0–29   → "Freshman"
    ///   30–59  → "Sophomore"
    ///   60–89  → "Junior"
    ///   90+    → "Senior"
    pub fn class_standing(&self) -> &str {
        // Check the credit limits from lowest to highest.
        if self.credits_earned < 30 {
            "Freshman"
        } else if self.credits_earned < 60 {
            "Sophomore"
        } else if self.credits_earned < 90 {
            "Junior"
        } else {
            "Senior"
        }
    }

    /// Adds `credits` to the student's `credits_earned` total.
    pub fn add_credits(&mut self, credits: u16) {
        self.credits_earned += credits; // Add to the existing total.
    }

    /// Returns `true` if the student has earned 120 or more credits.
    pub fn can_graduate(&self) -> bool {
        self.credits_earned >= 120 // This comparison returns true or false.
    }

    /// Appends `course_grade` to the student's `grades` vector.
    pub fn add_grade(&mut self, course_grade: CourseGrade) {
        self.grades.push(course_grade); // push adds an item to the end of a vector.
    }

    /// Returns the student's GPA as a weighted average using quality points.
    /// Returns 0.0 if the student has no grades.
    /// GPA = total quality points / total credit hours
    pub fn calculate_gpa(&self) -> f32 {
        let mut total_quality_points = 0.0;
        let mut total_credits = 0.0;

        // Borrow each course with & so it stays in the student's grades list.
        for course in &self.grades {
            total_quality_points += course.quality_points();
            total_credits += course.credits as f32; // Convert credits to a decimal number.
        }

        if total_credits == 0.0 {
            return 0.0; // Avoid division by zero when there are no credit hours.
        }

        total_quality_points / total_credits
    }
}

impl Grade {
    /// Returns the GPA points for this letter grade:
    ///   A → 4.0, B → 3.0, C → 2.0, D → 1.0, F → 0.0
    pub fn to_gpa_points(&self) -> f32 {
        // match chooses the number that belongs to this enum variant.
        match self {
            Grade::A => 4.0,
            Grade::B => 3.0,
            Grade::C => 2.0,
            Grade::D => 1.0,
            Grade::F => 0.0,
        }
    }

    /// Parses a grade from a string (case-insensitive).
    /// Returns `None` for unrecognised inputs.
    pub fn from_string(s: &str) -> Option<Grade> {
        // Accept either letter case. Some holds a valid grade; None means invalid input.
        match s {
            "A" | "a" => Some(Grade::A),
            "B" | "b" => Some(Grade::B),
            "C" | "c" => Some(Grade::C),
            "D" | "d" => Some(Grade::D),
            "F" | "f" => Some(Grade::F),
            _ => None, // The wildcard covers every other input.
        }
    }

    /// Returns `true` for grades A, B, and C; `false` for D and F.
    pub fn is_passing(&self) -> bool {
        // The | symbol allows any of these three grades to count as passing.
        matches!(self, Grade::A | Grade::B | Grade::C)
    }
}

impl CourseGrade {
    /// Creates a new CourseGrade.
    pub fn new(
        course_code: String,
        course_name: String,
        credits: u16,
        grade: Grade,
    ) -> CourseGrade {
        // A field and parameter with the same name can be written just once.
        CourseGrade {
            course_code,
            course_name,
            credits,
            grade,
        }
    }

    /// Returns the quality points for this course: credits × GPA points.
    pub fn quality_points(&self) -> f32 {
        self.credits as f32 * self.grade.to_gpa_points()
    }
}

impl StudentDatabase {
    /// Creates a new, empty database.
    pub fn new() -> StudentDatabase {
        StudentDatabase {
            students: HashMap::new(), // Store students using their IDs as keys.
        }
    }

    /// Adds a student to the database.
    /// Returns `Err` if a student with the same id already exists.
    pub fn add_student(&mut self, student: Student) -> Result<(), String> {
        if self.students.contains_key(&student.id) {
            return Err(String::from("A student with this ID already exists."));
        }

        // Copy the ID for the key, then move the whole student into the database.
        self.students.insert(student.id.clone(), student);
        Ok(()) // An empty success value means the student was added.
    }

    /// Returns a reference to the student with the given id, or `None`.
    pub fn find_student(&self, id: &str) -> Option<&Student> {
        self.students.get(id) // Borrow the student, or return None if the ID is missing.
    }

    /// Returns a mutable reference to the student with the given id, or `None`.
    pub fn find_student_mut(&mut self, id: &str) -> Option<&mut Student> {
        self.students.get_mut(id) // A mutable reference lets the caller update the student.
    }

    /// Returns the total number of students in the database.
    pub fn student_count(&self) -> usize {
        self.students.len() // len returns the number of entries in the map.
    }

    /// Returns the average GPA across all students.
    /// Returns 0.0 if there are no students.
    pub fn average_gpa(&self) -> f32 {
        if self.students.is_empty() {
            return 0.0; // An empty database has no GPAs to average.
        }

        let mut total_gpa = 0.0;
        // values visits the students without including their ID keys.
        for student in self.students.values() {
            total_gpa += student.calculate_gpa();
        }

        total_gpa / self.student_count() as f32
    }

    /// Returns a vector of references to all students in the database.
    pub fn list_students(&self) -> Vec<&Student> {
        let mut students = Vec::new();
        for student in self.students.values() {
            students.push(student); // Store references so the database keeps ownership.
        }
        students
    }
}

// ============================================================================
// TESTS: DO NOT MODIFY
// ============================================================================
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_student_creation() {
        let student = Student::new(
            String::from("S001"),
            String::from("Test Student"),
            String::from("test@example.com"),
        );
        assert_eq!(student.id, "S001");
        assert_eq!(student.name, "Test Student");
        assert_eq!(student.credits_earned, 0);
        assert!(student.grades.is_empty());
    }

    #[test]
    fn test_class_standing() {
        let mut student = Student::new(
            String::from("S001"),
            String::from("Test"),
            String::from("test@example.com"),
        );
        assert_eq!(student.class_standing(), "Freshman");

        student.add_credits(30);
        assert_eq!(student.class_standing(), "Sophomore");

        student.add_credits(30);
        assert_eq!(student.class_standing(), "Junior");

        student.add_credits(30);
        assert_eq!(student.class_standing(), "Senior");
    }

    #[test]
    fn test_graduation_eligibility() {
        let mut student = Student::new(
            String::from("S001"),
            String::from("Test"),
            String::from("test@example.com"),
        );
        assert!(!student.can_graduate());

        student.add_credits(120);
        assert!(student.can_graduate());
    }

    #[test]
    fn test_grade_parsing() {
        assert_eq!(Grade::from_string("A"), Some(Grade::A));
        assert_eq!(Grade::from_string("a"), Some(Grade::A));
        assert_eq!(Grade::from_string("B"), Some(Grade::B));
        assert_eq!(Grade::from_string("F"), Some(Grade::F));
        assert_eq!(Grade::from_string("Z"), None);
        assert_eq!(Grade::from_string(""), None);
    }

    #[test]
    fn test_grade_gpa_points() {
        assert_eq!(Grade::A.to_gpa_points(), 4.0);
        assert_eq!(Grade::B.to_gpa_points(), 3.0);
        assert_eq!(Grade::C.to_gpa_points(), 2.0);
        assert_eq!(Grade::D.to_gpa_points(), 1.0);
        assert_eq!(Grade::F.to_gpa_points(), 0.0);
    }

    #[test]
    fn test_passing_grades() {
        assert!(Grade::A.is_passing());
        assert!(Grade::B.is_passing());
        assert!(Grade::C.is_passing());
        assert!(!Grade::D.is_passing());
        assert!(!Grade::F.is_passing());
    }

    #[test]
    fn test_quality_points() {
        let course = CourseGrade::new(String::from("IS4010"), String::from("App Dev"), 3, Grade::A);
        assert_eq!(course.quality_points(), 12.0);

        let course2 = CourseGrade::new(
            String::from("IS3050"),
            String::from("Database"),
            4,
            Grade::B,
        );
        assert_eq!(course2.quality_points(), 12.0);
    }

    #[test]
    fn test_gpa_calculation() {
        let mut student = Student::new(
            String::from("S001"),
            String::from("Test"),
            String::from("test@example.com"),
        );

        assert_eq!(student.calculate_gpa(), 0.0);

        student.add_grade(CourseGrade::new(
            String::from("CS101"),
            String::from("Intro"),
            3,
            Grade::A,
        ));
        assert_eq!(student.calculate_gpa(), 4.0);

        student.add_grade(CourseGrade::new(
            String::from("CS102"),
            String::from("Data Structures"),
            3,
            Grade::B,
        ));
        assert_eq!(student.calculate_gpa(), 3.5);
    }

    #[test]
    fn test_database_add_student() {
        let mut db = StudentDatabase::new();
        let student = Student::new(
            String::from("S001"),
            String::from("Test"),
            String::from("test@example.com"),
        );

        assert!(db.add_student(student).is_ok());
        assert_eq!(db.student_count(), 1);
    }

    #[test]
    fn test_database_duplicate_student() {
        let mut db = StudentDatabase::new();
        let student1 = Student::new(
            String::from("S001"),
            String::from("Test1"),
            String::from("test1@example.com"),
        );
        let student2 = Student::new(
            String::from("S001"),
            String::from("Test2"),
            String::from("test2@example.com"),
        );

        assert!(db.add_student(student1).is_ok());
        assert!(db.add_student(student2).is_err());
        assert_eq!(db.student_count(), 1);
    }

    #[test]
    fn test_database_find_student() {
        let mut db = StudentDatabase::new();
        let student = Student::new(
            String::from("S001"),
            String::from("Test"),
            String::from("test@example.com"),
        );
        db.add_student(student).unwrap();

        assert!(db.find_student("S001").is_some());
        assert!(db.find_student("S999").is_none());
    }

    #[test]
    fn test_database_average_gpa() {
        let mut db = StudentDatabase::new();
        assert_eq!(db.average_gpa(), 0.0);

        let mut student1 = Student::new(
            String::from("S001"),
            String::from("Alice"),
            String::from("alice@example.com"),
        );
        student1.add_grade(CourseGrade::new(
            String::from("CS101"),
            String::from("Intro"),
            3,
            Grade::A,
        ));

        let mut student2 = Student::new(
            String::from("S002"),
            String::from("Bob"),
            String::from("bob@example.com"),
        );
        student2.add_grade(CourseGrade::new(
            String::from("CS101"),
            String::from("Intro"),
            3,
            Grade::B,
        ));

        db.add_student(student1).unwrap();
        db.add_student(student2).unwrap();

        assert_eq!(db.average_gpa(), 3.5);
    }
}
