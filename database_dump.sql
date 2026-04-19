-- Vunoh Global AI Assistant Database Schema
-- Generated: April 19, 2026
-- SQLite Format

-- Create the Task table
CREATE TABLE IF NOT EXISTS assistant_task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_code VARCHAR(12) UNIQUE NOT NULL,
    intent VARCHAR(50) NOT NULL,
    entities TEXT NOT NULL,
    risk_score INTEGER NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    steps TEXT NOT NULL,
    whatsapp_msg TEXT NOT NULL,
    email_msg TEXT NOT NULL,
    sms_msg TEXT NOT NULL,
    assigned_to VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert 5 sample tasks with complete data

-- Sample Task 1: Document Verification
INSERT INTO assistant_task (task_code, intent, entities, risk_score, status, steps, whatsapp_msg, email_msg, sms_msg, assigned_to, created_at) VALUES (
    'VNH-517654',
    'verify_document',
    '{"document_type": "land title", "location": "Karen", "recipient": "User", "urgency": "standard"}',
    60,
    'Pending',
    '["Step 1: Verify your identity", "Step 2: Provide land title documents", "Step 3: Submit for legal review", "Step 4: Await verification confirmation"]',
    'Hi! 👋 We received your land title verification request for your plot in Karen. Our legal team will review your documents within 24-48 hours. Expect an update via SMS. 📱',
    'Your land title verification request has been received and assigned to our Legal Team. Task Code: VNH-517654. Required documents have been noted: land title deed. Processing time: 24-48 hours.',
    'VNH-517654: Land title verification submitted. Legal team reviewing. You''ll get updates via email. -Vunoh',
    'Legal Team',
    '2026-04-19 08:30:00'
);

-- Sample Task 2: Money Transfer (Urgent)
INSERT INTO assistant_task (task_code, intent, entities, risk_score, status, steps, whatsapp_msg, email_msg, sms_msg, assigned_to, created_at) VALUES (
    'VNH-6BDCEE',
    'send_money',
    '{"amount": "15000", "currency": "KES", "recipient": "sister", "location": "Kisumu", "urgency": "urgent"}',
    50,
    'Pending',
    '["Step 1: Verify recipient details", "Step 2: Confirm transfer amount and fees", "Step 3: Process payment", "Step 4: Send confirmation to recipient"]',
    'Hey! 💰 Your money transfer request is here. Sending KES 15,000 to Kisumu. Our Finance team is processing this right now. You''ll get a confirmation soon! ✅',
    'Urgent money transfer request received. Task Code: VNH-6BDCEE. Amount: KES 15,000. Recipient: Kisumu. Our Finance Team is prioritizing this request. Estimated completion: 2-4 hours.',
    'VNH-6BDCEE: KES 15K transfer to Kisumu submitted. Finance team processing. Confirmation coming. -Vunoh',
    'Finance Team',
    '2026-04-19 08:45:00'
);

-- Sample Task 3: Service Hiring
INSERT INTO assistant_task (task_code, intent, entities, risk_score, status, steps, whatsapp_msg, email_msg, sms_msg, assigned_to, created_at) VALUES (
    'VNH-8F2K9L',
    'hire_service',
    '{"service_type": "cleaning", "location": "Westlands", "urgency": "scheduled", "date": "Friday"}',
    25,
    'In Progress',
    '["Step 1: Match with available cleaners", "Step 2: Confirm service details and pricing", "Step 3: Schedule appointment", "Step 4: Send completion confirmation"]',
    'Great! 🧹 We found a cleaner for your Westlands apartment. Scheduled for Friday. Our Operations team will send you the cleaner''s details soon. Any changes? Just let us know! 📞',
    'Service hire request confirmed. Task Code: VNH-8F2K9L. Service: Professional cleaning. Location: Westlands. Scheduled: Friday. Operations team will coordinate directly with you.',
    'VNH-8F2K9L: Cleaner matched for Westlands Friday cleaning. Details coming via WhatsApp. -Vunoh',
    'Operations Team',
    '2026-04-19 09:15:00'
);

-- Sample Task 4: Airport Transfer
INSERT INTO assistant_task (task_code, intent, entities, risk_score, status, steps, whatsapp_msg, email_msg, sms_msg, assigned_to, created_at) VALUES (
    'VNH-4J7M2Q',
    'get_airport_transfer',
    '{"airport": "JKIA", "location": "Nairobi", "time": "10:00 AM", "passenger_count": "1"}',
    30,
    'Pending',
    '["Step 1: Confirm passenger details", "Step 2: Match with available driver", "Step 3: Arrange vehicle and route", "Step 4: Send driver contact and confirmation"]',
    'We''ve got your airport transfer! 🚕 Pickup from JKIA at 10:00 AM. Our Operations team is arranging your vehicle now. Driver details coming in a few mins. Safe travels! ✈️',
    'Airport transfer booking confirmed. Task Code: VNH-4J7M2Q. Pickup: JKIA at 10:00 AM. Driver and vehicle details will be sent via SMS and WhatsApp. Thank you for choosing Vunoh!',
    'VNH-4J7M2Q: JKIA pickup 10AM booked. Driver details coming. Check WhatsApp for updates. -Vunoh',
    'Operations Team',
    '2026-04-19 09:30:00'
);

-- Sample Task 5: Document Verification (Multiple)
INSERT INTO assistant_task (task_code, intent, entities, risk_score, status, steps, whatsapp_msg, email_msg, sms_msg, assigned_to, created_at) VALUES (
    'VNH-C1K5P9',
    'verify_document',
    '{"document_type": "national ID", "location": "Nairobi", "recipient": "User", "urgency": "standard"}',
    55,
    'Completed',
    '["Step 1: Collect ID copy", "Step 2: Verify with relevant authorities", "Step 3: Check for authenticity", "Step 4: Provide verification certificate"]',
    'Perfect! ✅ Your national ID verification is complete! The certificate is ready and will be sent to your email. You can also collect it from our Nairobi office. Thanks for using Vunoh! 🎉',
    'Your national ID verification has been COMPLETED. Task Code: VNH-C1K5P9. Verification certificate attached. Valid for 2 years. For renewal, contact us anytime.',
    'VNH-C1K5P9: ID verification complete! Certificate sent to email. Valid 2 years. -Vunoh',
    'Legal Team',
    '2026-04-19 07:00:00'
);

-- Create indexes for common queries
CREATE INDEX IF NOT EXISTS idx_task_code ON assistant_task(task_code);
CREATE INDEX IF NOT EXISTS idx_intent ON assistant_task(intent);
CREATE INDEX IF NOT EXISTS idx_status ON assistant_task(status);
CREATE INDEX IF NOT EXISTS idx_assigned_to ON assistant_task(assigned_to);
CREATE INDEX IF NOT EXISTS idx_created_at ON assistant_task(created_at);

-- Verify data integrity
SELECT COUNT(*) as total_tasks FROM assistant_task;
SELECT intent, COUNT(*) as count FROM assistant_task GROUP BY intent;
SELECT status, COUNT(*) as count FROM assistant_task GROUP BY status;
