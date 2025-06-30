import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewQuitModComponent } from './new-quit-mod.component';

describe('NewQuitModComponent', () => {
  let component: NewQuitModComponent;
  let fixture: ComponentFixture<NewQuitModComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NewQuitModComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NewQuitModComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
